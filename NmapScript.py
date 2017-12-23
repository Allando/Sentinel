#!/bin/python

"""
This is a script which uses nmap through shell command.'
"""

# Standard libraries
import os
import subprocess
import xml.etree.ElementTree as ET

# Third party libraries


class Nmap:
    def __init__(self, ip_range):
        self.ip_range = ip_range
        self.filepath = os.path.abspath("temp/nmap_output.xml")

    def scan(self, port_range=None, arguments=None):
        command_line = "nmap {} -oX -".format(self.ip_range)

        if port_range is None and arguments is None:
            command_line = command_line
        elif port_range is not None and arguments is None:
            command_line = command_line + " -p {}".format(port_range)
        elif port_range is None and arguments is not None:
            command_line = command_line + " " + arguments
        elif port_range is not None and arguments is not None:
            command_line = command_line + " -p {} {}".format(port_range, arguments)
        else:
            print("Check ya input again...")

        f = open(self.filepath, "w")
        subprocess.run(command_line, stdout=f, shell=True)
        f.close()

    def print_output(self):
        tree = ET.parse(self.filepath)
        root = tree.getroot()
        print(root)

        for child in root:
            print(child.tag, child.attrib)

        # ports = dom.findall('nmaprun/host/ports/port/state')


ippo_nmap = Nmap("192.168.6.86")
ippo_nmap.scan(arguments="-v -A -Pn")
ippo_nmap.print_output()
