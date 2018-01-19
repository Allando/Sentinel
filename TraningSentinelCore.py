"""
This is the Convolutional Neural Network module of Sentinel

Concept: #5

Input: Open ports or Software or Kernel... which basically is software but whatever.
Output: Exploitable || Inexploitable
"""

# Standard Libraries
import subprocess
import sys

# Third Party Libraries
import numpy as np


class SentinelCore:
    def __init__(self, sizes):
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    """
    This 
    """
    def feed_forward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = self.activation(np.dot(w, a)+b)

    def SGD(self, epochs, ):
        pass

    def backprop(self):
        pass

    """
    Takes in z and a mode parameters
    Where:
        z is the activation, weights and bias.
        mode specifies which activation function is being used.
        
    Return:
        The result of which activation function is used.
    """
    @staticmethod
    def activation(z, mode=None):
        if mode == 's' or 'S' or None:
            return 1.0 / (1.0 + np.exp(-z))
        elif mode == 'r' or 'R':
            pass
            # TODO: Return ReLU