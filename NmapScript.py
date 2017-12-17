#!/bin/python

"""
This is a script which uses nmap through shell command.'
"""

# Standard libraries
import subprocess

# Third party libraries
import numpy as np


class Nmap:
    def __init__(self, ip_range):
        self.ip_range = ip_range
        self.filepath = "temp/nmap_output.xml"

    def scan(self, port_range=None, arguments=None):
        command_line = "nmap {} -oX -".format(self.ip_range)

        if port_range == None and arguments == None:
            command_line = command_line
        elif port_range != None and arguments == None:
            command_line = command_line + " -p {}".format(port_range)
        elif port_range == None and arguments != None:
            command_line = command_line + " " + arguments
        elif port_range != None and arguments != None:
            command_line = command_line + " -p {} {}".format(port_range, arguments)
        else:
            print("Check ya input again...")

        f = open(self.filepath, "w")
        subprocess.run(command_line, stdout=f, shell=True)
        f.close()

    def print_output(self):
        pass


IppoNmap = Nmap("192.168.0.108")
scanning = IppoNmap.scan("21-24", "-Pn")

print(IppoNmap.print_output())
