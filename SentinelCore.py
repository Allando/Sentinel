"""
This is the Convolutional Neural Network module of Sentinel

Concept: #5

Input: Open ports or Software or Kernel... which basically is software but whatever.
Output: Exploitable || Inexploitable
"""

# Standard Libraries
import platform
import os

# Third Party Libraries
import numpy as np


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

    def feed_forward(self):
        

    def SGD(self):
        pass

    def cost_function(self, w, b):
        return np.sum(w, b)

    def backprop(self):
        pass

    # Activation functions

    def sigmoid(self, z):
        return 1.0 / (1.0+np.exp(-z))

    def ReLU(self, z):
        pass
