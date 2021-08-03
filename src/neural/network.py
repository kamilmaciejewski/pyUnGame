import collections
from random import randrange

from src import ung_globals
from src.neural.neuron import *
from src.neural.neuronConnection import NeuronConnection
from src.utils import geometry


class Network:
    neurons = list
    n_id = int
    size = int
    shape_surf = pygame.Surface
    tmp = dict

    def __init__(self, n_id, size):
        self.n_id = n_id
        self.neurons = list()

        for i in range(size):
            self.neurons.append(Neuron(str(self.n_id) + ":" + str(i), (randrange(1, 255), randrange(1, 255), 10, 10)))

        for neuron in self.neurons:
            connections = dict()

            for neuron0 in self.neurons:
                if not id(neuron) == id(neuron0):
                    connections[geometry.calculate_distance(neuron0.body.center, neuron.body.center)] = neuron0

            sorted_connections = collections.OrderedDict(sorted(connections.items()))

            for k, v in sorted_connections.items():
                if len(neuron.connections) < ung_globals.neuronConnections:
                    neuron.connections.append(NeuronConnection(v, k))

        self.shape_surf = pygame.Surface((255, 255), pygame.SRCALPHA)
        pygame.draw.rect(self.shape_surf, pygame.Color(128, 128, 128), self.shape_surf.get_rect(), 1)

    def draw(self, screen: pygame.surface):
        screen.blit(self.shape_surf, (0, 0))
        for neuron in self.neurons:
            neuron.draw(screen)

    def update(self):
        for neuron in self.neurons:
            neuron.calculate()
