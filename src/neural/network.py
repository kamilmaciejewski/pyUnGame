import collections
from random import randrange

import numpy

from src import ung_globals
from src.neural.networkData import NetworkData
from src.neural.neuron import *
from src.neural.neuronConnection import NeuronConnection
from src.utils import geometry


# def lam(neuron: Neuron):
#     return neuron.calculate()


class Network:
    data = NetworkData
    neurons = list
    n_id = int
    size = int
    shape_surf = pygame.Surface
    tmp = dict

    def __init__(self, n_id, size):
        self.data = NetworkData(size)
        self.n_id = n_id
        self.neurons = list()
        # self.neurons_data_res = numpy.zeros(size)
        # self.neurons_data = numpy.random.rand(size)


        for i in range(size):
            self.neurons.append(
                Neuron(i,
                       NetworkDataHandler(i, self.data),
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
                    self.data.neurons_weights[neuron.n_id, v.n_id] = (k * 0.01)
                else:
                    break

        self.shape_surf = pygame.Surface((255, 255), pygame.SRCALPHA)
        pygame.draw.rect(self.shape_surf, pygame.Color(128, 128, 128), self.shape_surf.get_rect(), 1)

    def draw(self, screen: pygame.surface):

        for neuron in self.neurons:
            neuron.draw(self.shape_surf)
        screen.blit(self.shape_surf, (0, 100))

    def update(self):
        # for neuron in self.neurons:
        #    neuron.calculate()
        self.data.neurons_data = self.data.neurons_data * self.data.neurons_is_input
        self.data.neurons_data = self.data.neurons_data + numpy.dot(self.data.neurons_data, self.data.neurons_weights.T)
        self.data.neurons_thresholds = self.data.neurons_thresholds - \
                                       (self.data.neurons_thresholds_delta * numpy.invert(self.data.neurons_is_input) *
                                        (self.data.neurons_data < self.data.neurons_thresholds))

        # list(map(lam, self.neurons))
        # return self.n_id

    def make_input(self, n_id: int):
        self.data.neurons_is_input[n_id] = True
        self.data.neurons_weights[n_id].fill(0.)
        self.data.neurons_thresholds[n_id] = 0.
        for conn in self.neurons[n_id].connections:
            conn.weight = 0.
