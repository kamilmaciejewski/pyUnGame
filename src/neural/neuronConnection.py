from src.neural.neuron import Neuron
import ung_globals
import logging


class NeuronConnection:
    weight = float
    n = Neuron

    def __init__(self, n: Neuron, w: float):
        self.n = n
        self.weight = (1/0.001+w) * (ung_globals.connectionWeightUnit / ung_globals.neuronConnections)
        #logging.info("Neuron connection " + str(self.weight) + " created")
        # log("neuron", "Neuron connection " + str(self.weight) + " created")

    def calculate(self):
        return self.weight * self.n.val

