"""
This is the Convolutional Neural Network module of Sentinel

Concept: #5

Input: Open ports or Software or Kernel... which basically is software but whatever.
Output: Exploitable || Inexploitable
"""

# Standard Libraries
import binascii
import os
import subprocess
import sys

# Third Party Libraries
import numpy as np
import zipfile


class SentinelCore:
    def __init__(self, sizes):
        self.weights = np.random.randn()
        self.biases = np.random.randn()
        self.nmbr_of_layers = len(sizes)
        self.sizes = sizes

    def activation(self, a):
        return self.sigmoid(np.dot(self.weights, a)+self.biases)
    """
        w = weight
        b = bias
        a = activation from previous layer
    """

    def feed_forward(self, a):
        """Return the output of the network if ``a`` is input."""
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid(np.dot(w, a) + b)
        return a

    def SGD(self, input_data, ):
        pass
        # TODO: Take input
        # TODO: Randomize input
        # TODO: Calculate derivative Cost / derivative weights and dCost / dBias

    def cost_function(self, w, b):
        return np.sum(w, b)

    def backprop(self):
        pass
        # TODO: Add the whole thing

    # For local mode
    @staticmethod
    def program_input(path_to_file):
        with open("testin.dat", "w") as f:
            command_line = "./{}".format(path_to_file)
            subprocess.run(command_line, stdout=f, shell=True)




    # For network mode
    @staticmethod
    def ports_input():
        pass
    # Activation functions

    @staticmethod
    def sigmoid(z):
        return 1.0 / (1.0+np.exp(-z))

    def ReLU(self, z):
        pass
        # TODO: Implement ReLU


testCore1 = SentinelCore.program_input("Data/StackBufferOverflow")