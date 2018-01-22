from subprocess import *


class SystemMode:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file



    def input(self):
        command_line = './{}'.format(self.path_to_file)

        target = Popen(command_line, shell=True, stderr=STDOUT)
        return target


