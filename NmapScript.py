#!/bin/python

"""
This is a script which uses nmap through shell command.'
"""

# Standard libraries
import os

# Third party libraries
import numpy as np


class Nmap:
    def __init__(self, ip_range, port_range=None, commands=None):
        self.ip_range = ip_range
        self.port_range = port_range
        self.commands = commands

    def scan_network(self):
        if self.port_range is not None:
            return os.system("sudo nmap {} -p {} {}".format(self.ip_range, self.port_range, self.commands))
        else:
            return os.system("sudo nmap {} {}".format(self.ip_range, self.commands))


hosts = "10.200.126.0/24"
nm0 = Nmap(hosts)
nm1 = Nmap(hosts, "21-23", "-sn")
nm2 = Nmap(hosts, "21-23")
nm3 = Nmap(hosts, "21", "-sn")
nm4 = Nmap(hosts, "21")

print("0: ", nm0.scan_network())
print("1: ", nm1.scan_network())
print("2: ", nm2.scan_network())
print("3: ", nm3.scan_network())
print("4: ", nm4.scan_network())

