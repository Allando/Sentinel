#!/bin/python

"""
This is a script which uses nmap through shell command.'
"""

# Standard libraries
import os

# Third party libraries
import numpy as np
import nmap

nm = nmap.PortScanner() # instantiate nmap.PortScanner object
nm.scan('192.168.0.0/24')

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        for port in lport:
            if nm[host][proto][port]['state'] == 'open':
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
