import collections
from random import randrange

import numpy
from pygame import Color

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

    def __init__(self, n_id: int, size: int):
        self.data = NetworkData(size)
        self.n_id = n_id
        self.neurons = list()
        # self.neurons_data_res = numpy.zeros(size)
        # self.neurons_data = numpy.random.rand(size)

        for i in range(size):
            self.neurons.append(
                Neuron(i,
                       NetworkDataHandler(i, self.data),
                       (
                           randrange(1, ung_globals.network_geometry_size),
                           randrange(1, ung_globals.network_geometry_size),
                           5, 5)))
            if i < 5:
                self.make_input(i)
                self.neurons[i].data_handler.set_val(0.5)

        for neuron in self.neurons:
            if neuron.is_input():
                continue
            connections = dict()

            for neuron0 in self.neurons:
                if not id(neuron) == id(neuron0):
                    connections[geometry.calculate_distance(neuron0.body.center, neuron.body.center)] = neuron0

            sorted_connections = collections.OrderedDict(sorted(connections.items()))

            for k, v in sorted_connections.items():
                if len(neuron.connections) < ung_globals.neuronConnections:
                    neuron.connections.append(NeuronConnection(v))
                    self.data.neurons_weights[neuron.n_id, v.n_id] = (k * 0.001)
                else:
                    break

        self.shape_surf = pygame.Surface((ung_globals.network_geometry_size, ung_globals.network_geometry_size),
                                         pygame.SRCALPHA)
        pygame.draw.rect(self.shape_surf, pygame.Color(128, 128, 128), self.shape_surf.get_rect(), 1)

    def draw(self, screen: pygame.surface):

        for neuron in self.neurons:
            neuron.draw(self.shape_surf)
        screen.blit(self.shape_surf, (0, 100))
        self.shape_surf.fill(Color(0, 0, 0, 0))

    def update(self):
        # for neuron in self.neurons:
        #    neuron.calculate()

        input_data = numpy.dot(self.data.neurons_data * self.data.neurons_is_input,
                               self.data.neurons_weights.T)  # get data from input
        is_enabled = (self.data.neurons_data > self.data.neurons_thresholds)

        non_input_data_base = self.data.neurons_data * numpy.invert(
            numpy.invert(self.data.neurons_is_input) * is_enabled)
        non_input_data = numpy.dot(non_input_data_base,
                                   self.data.neurons_weights.T)  # get data from non input (only if neuron is enabled)

        self.data.neurons_data = self.data.neurons_data * self.data.neurons_is_input  # clean data for non input
        self.data.neurons_data = self.data.neurons_data + input_data + non_input_data

        threshold_delta = self.data.neurons_thresholds_delta * numpy.invert(self.data.neurons_is_input)
        is_enabled = (self.data.neurons_data > self.data.neurons_thresholds)
        delta_enabled = threshold_delta * numpy.invert(is_enabled)
        delta_disabled = threshold_delta * is_enabled

        self.data.neurons_thresholds = self.data.neurons_thresholds - delta_enabled + delta_disabled

        # list(map(lam, self.neurons))
        # return self.n_id

    def make_input(self, n_id: int):
        self.data.neurons_is_input[n_id] = True
        self.data.neurons_weights[n_id].fill(0.)
        self.data.neurons_thresholds[n_id] = 0.
        for conn in self.neurons[n_id].connections:
            conn.weight = 0.
