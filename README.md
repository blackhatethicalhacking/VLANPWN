# VLANPWN
VLAN attacks toolkit

**The author has nothing to do with those who will use these tools for personal purposes to destroy other people's computer networks. The tools are presented for training purposes to help engineers improve the security of their network.**

**ᛝ**

**DoubleTagging.py** - This tool is designed to carry out a VLAN Hopping attack. As a result of injection of a frame with two 802.1Q tags, a test ICMP request will also be sent.

**DTPHijacking.py** - A script for conducting a DTP Switch Spoofing/Hijacking attack. Sends a malicious DTP-Desirable frame, as a result of which the attacker's machine becomes a trunk channel. The impact of this attack is that you can bypass the segmentation of VLAN networks and see all the traffic of VLAN networks.

```
python3 DoubleTagging.py --help

.s    s.  .s        .s5SSSs.  .s    s.  .s5SSSs.  .s s.  s.  .s    s.
      SS.                 SS.       SS.       SS.    SS. SS.       SS.
sS    S%S sS        sS    S%S sSs.  S%S sS    S%S sS S%S S%S sSs.  S%S
SS    S%S SS        SS    S%S SS`S. S%S SS    S%S SS S%S S%S SS`S. S%S
SS    S%S SS        SSSs. S%S SS `S.S%S SS .sS::' SS S%S S%S SS `S.S%S
 SS   S%S SS        SS    S%S SS  `sS%S SS        SS S%S S%S SS  `sS%S
 SS   `:; SS        SS    `:; SS    `:; SS        SS `:; `:; SS    `:;
  SS  ;,. SS    ;,. SS    ;,. SS    ;,. SS        SS ;,. ;,. SS    ;,.
   `:;;:' `:;;;;;:' :;    ;:' :;    ;:' `:        `:;;:'`::' :;    ;:'

VLAN Double Tagging inject tool. Jump into another VLAN!

Author: Magama Bazarov, <in9uz@protonmail.com>

usage: DoubleTagging.py [-h] --interface INTERFACE --nativevlan NATIVEVLAN --targetvlan TARGETVLAN --victim VICTIM --attacker ATTACKER

options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Specify your network interface
  --nativevlan NATIVEVLAN
                        Specify the Native VLAN ID
  --targetvlan TARGETVLAN
                        Specify the target VLAN ID for attack
  --victim VICTIM       Specify the target IP
  --attacker ATTACKER   Specify the attacker IP
  ```
  Example:
  
  ```
  python3 DoubleTagging.py --interface eth0 --nativevlan 1 --targetvlan 20 --victim 10.10.20.24 --attacker 10.10.10.54
  ```
  
  ```
  python3 DTPHijacking.py --help
  
.s    s.  .s        .s5SSSs.  .s    s.  .s5SSSs.  .s s.  s.  .s    s.
      SS.                 SS.       SS.       SS.    SS. SS.       SS.
sS    S%S sS        sS    S%S sSs.  S%S sS    S%S sS S%S S%S sSs.  S%S
SS    S%S SS        SS    S%S SS`S. S%S SS    S%S SS S%S S%S SS`S. S%S
SS    S%S SS        SSSs. S%S SS `S.S%S SS .sS::' SS S%S S%S SS `S.S%S
 SS   S%S SS        SS    S%S SS  `sS%S SS        SS S%S S%S SS  `sS%S
 SS   `:; SS        SS    `:; SS    `:; SS        SS `:; `:; SS    `:;
  SS  ;,. SS    ;,. SS    ;,. SS    ;,. SS        SS ;,. ;,. SS    ;,.
   `:;;:' `:;;;;;:' :;    ;:' :;    ;:' `:        `:;;:'`::' :;    ;:'

DTP Switch Hijacking tool. Become a trunk!

Author: Magama Bazarov, <in9uz@protonmail.com>

usage: DTPHijacking.py [-h] --interface INTERFACE

options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Specify your network interface
```
Example:

```
python3 DTPHijacking.py --interface eth0
```
