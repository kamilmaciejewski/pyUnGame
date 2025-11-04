import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from neural.neuron import Neuron
import ung_globals
import pygame

class NeuronConnection:
    weight = float
    n = Neuron
    col = pygame.Color

    def __init__(self, n: Neuron, w: float):
        self.n = n
        # TODO: weight should depend on the distance bwetwwn neurons
        self.weight = min( 0.75/(w + 0.00001), 0.075) #* (ung_globals.connectionWeightUnit / ung_globals.neuronConnections)
        #logging.info("Neuron connection " + str(self.weight) + " created")
        # log("neuron", "Neuron connection " + str(self.weight) + " created")
        val = int(min(self.weight*2000, 255))
        self.col =  pygame.Color(val, val, val)

    def calculate(self):
        return self.weight * self.n.val

