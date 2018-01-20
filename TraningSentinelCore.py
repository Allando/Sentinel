"""
This is the Convolutional Neural Network module of Sentinel

Concept: #5

Input: Open ports or Software or Kernel... which basically is software but whatever.
Output: Exploitable || Inexploitable
"""

# Standard Libraries
import random

# Third Party Libraries
import numpy as np


class SentinelCore:
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feed_forward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = activation_function(np.dot(w, a) + b)
        return a

    def sgd(self, epochs, eta, input_data, mini_batch_size):
        desired_result = "root"

        traning_data = list(input_data)
        lengh_traning_data = len(traning_data)

        for j in range(epochs):
            random.shuffle(traning_data)
            mini_batches = [
                traning_data[k:k + mini_batch_size]
                for k in range(0, lengh_traning_data, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if desired_result:
                print("Epoch {} : {} / {}".format(j, self.evaluate(desired_result), 1))
            else:
                print("Epoch {} complete".format(j))

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

        self.biases = [b - (eta / len(mini_batch)) * nb for b, nb in zip(self.biases, nabla_b)]
        self.weights = [w - (eta / len(mini_batch)) * nw for w, nw in zip(self.weights, nabla_w)]

    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        # feedforward
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = activation(z)
            activations.append(activation)

        # backward pass
        delta = self.cost_derivative(activation[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for l in range(2, self.num_layers):
            z = zs[-1]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l + 1].transpose(), delta) * sp
            nabla_b[-1] = delta
            nabla_w[-1] = np.dot(delta, activations[-l - 1].transpose())

        return nabla_b, nabla_w

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feed_forward(x)), y) for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    @staticmethod
    def cost_derivative(output_activations, y):
        return output_activations - y


def activation_function(z, mode=None):
    """
    Takes in z and a mode parameters
    Where:
        z is the activation, weights and bias.
        mode specifies which activation function is being used.

    Return:
        The result of which activation function is used.
    """
    if mode == 's' or 'S' or None:
        return 1.0 / (1.0 + np.exp(-z))
    elif mode == 'r' or 'R':
        pass
        # TODO: Return ReLU


def sigmoid_prime(z):
    return activation_function(z) * (1 - activation_function(z))
