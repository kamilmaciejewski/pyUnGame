from neuron import *


class Network:
    neurons = []

    def __init__(self, size):
        print("Network created")
        for _ in range(size):
            self.neurons.append(Neuron())

    def update(self):
        for neuron in self.neurons:
            neuron.calculate()
