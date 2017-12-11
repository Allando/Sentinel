#!/bin/python

"""
This is a script which uses nmap through shell command.'
"""

# Standart libraries
import os

# Third party libraries
import numpy as np

ip_address = "192.168.0.108"
ports = np.array([21, 22, 23, 80, 445])

print(os.system("sudo nmap {} -O".format(ip_address)))
