"""
This is the Convolutional Neural Network module of Sentinel

Concept: 3

Input: Open ports
Output: Exploitable 1/0
"""

import numpy as np

class Sentinel_Core:

    def __init__(self, sizes):
        self.sizes = sizes
        self.num_layers = len(sizes)
        self.weights = [np.random.randn(y, 1) for y in sizes[1:]]
        sefl.biases = [np.random.randn(y, x)
                for x, y in zip(sizes[:-1], sizes[1:])]

    def sigmoid(self, a, w, b):
        return 1/(1+np.exp(-np.sum(w, a, -b)))

    def cost(self, w, b):
        
