"""
Test data model will substute actual targets for research purposes
"""

import numpy as np
import random
import threading

class TestData:
    def __init__(self, ports, services, result):
        self.ports = None
        self.services = services
        self.result = result

    def create_data(self):
        pass


    def write_to_file(self):
        with open('sentinel_training_data.txt', "w") as f:
            pass
