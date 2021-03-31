#!/usr/bin/env python3
from ipaddress import ip_address, IPv4Address, IPv6Address

ipchk = input("Apply an IP address: ")
try:
    res = ip_address(ipchk)
    if res == IPv4Address(ipchk):
        print("IPv4:", ipchk)
    elif res == IPv6Address(ipchk):
        print("IPv6: ", ipchk)
    else:
        print("You did not provide input.")
except:
    print("Error: Entry does not meet IPv4 or IPv6 Standard", IPv6Address(ipchk), IPv4Address(ipchk))


