from src import logger
from src.neural.neuron import *


class Network:
    neurons = []
    counter = 0
    n_id = 0

    def __init__(self, size, n_id):
        logger.log("Network " + str(self.n_id), "size " + str(size) + " created")
        for _ in range(size):
            self.neurons.append(Neuron())
        self.n_id = n_id

    def update(self):
        self.counter += 1
        for neuron in self.neurons:
            neuron.calculate()
