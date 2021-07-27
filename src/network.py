from src import logger
from src.neural.neuron import *


class Network:
    neurons = list
    counter = 0
    n_id = int

    def __init__(self, n_id, size):
        self.n_id = n_id
        self.neurons = list()
        logger.log("Network " + str(self.n_id), "size " + str(size) + " created")
        for i in range(size):
            logger.log("Network " + str(self.n_id), "neurons in net before: " + str(len(self.neurons)))
            logger.log("Network " + str(self.n_id), "add neuron " + str(i) + ":")
            self.neurons.append(Neuron(str(self.n_id) + ":" + str(i)))
            logger.log("Network " + str(self.n_id), "neurons in net after: " + str(len(self.neurons)))
        self.n_id = n_id

    def update(self):
        self.counter += 1
        logger.log("Network " + str(self.n_id), "size " + str(len(self.neurons)) + " update: " + str(self.counter))
        for neuron in self.neurons:
            neuron.calculate()
