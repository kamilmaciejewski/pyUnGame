import collections
from random import randrange

import numpy

from src import ung_globals
from src.neural.neuron import *
from src.neural.neuronConnection import NeuronConnection
from src.utils import geometry


def lam(neuron: Neuron):
    return neuron.calculate()


class Network:
    neurons_data = numpy.array
    neurons_data_res = numpy.array
    neurons_wages = numpy.array
    neurons_thresholds = numpy.array
    neurons = list
    n_id = int
    size = int
    shape_surf = pygame.Surface
    tmp = dict

    def __init__(self, n_id, size):
        self.n_id = n_id
        self.neurons = list()
        self.neurons_data_res = numpy.zeros(size)
        # self.neurons_data = numpy.random.rand(size)
        self.neurons_data = numpy.zeros(size)
        self.neurons_is_input = numpy.full(size, False)
        self.neurons_thresholds = numpy.full(size, 0.5)
        self.neurons_weights = numpy.zeros((size, size))

        for i in range(size):
            self.neurons.append(
                Neuron(i,
                       NetworkDataHandler(i, self.neurons_data, self.neurons_data_res, self.neurons_weights[i],
                                          self.neurons_thresholds, self.neurons_is_input),
                       (randrange(1, 255), randrange(1, 255), 5, 5)))

        for neuron in self.neurons:
            connections = dict()

            for neuron0 in self.neurons:
                if not id(neuron) == id(neuron0):
                    connections[geometry.calculate_distance(neuron0.body.center, neuron.body.center)] = neuron0

            sorted_connections = collections.OrderedDict(sorted(connections.items()))

            for k, v in sorted_connections.items():
                if len(neuron.connections) < ung_globals.neuronConnections:
                    neuron.connections.append(NeuronConnection(v, k))
                    self.neurons_weights[neuron.n_id, v.n_id] = (k * 0.01)
                else:
                    break

        self.shape_surf = pygame.Surface((255, 255), pygame.SRCALPHA)
        pygame.draw.rect(self.shape_surf, pygame.Color(128, 128, 128), self.shape_surf.get_rect(), 1)

    def draw(self, screen: pygame.surface):

        for neuron in self.neurons:
            neuron.draw(self.shape_surf)
        screen.blit(self.shape_surf, (0, 100))

    def update(self):
        for neuron in self.neurons:
            neuron.calculate()
        self.neurons_data_res = numpy.dot(self.neurons_data, self.neurons_weights.T)
        # list(map(lam, self.neurons))
        #return self.n_id
