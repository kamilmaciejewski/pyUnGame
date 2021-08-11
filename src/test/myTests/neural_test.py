from random import randrange
import numpy
import unittest

from src.neural.network import Network
from src.neural.neuron import Neuron


class TestStringMethods(unittest.TestCase):
    def test_neuron_create(self):
        size = 2
        n_id = 42
        neurons_data_res = numpy.zeros(size)
        neurons_data = numpy.random.rand(size)
        neurons_wages = numpy.zeros((size, size))
        neuron = Neuron(n_id, neurons_data, neurons_wages, (randrange(1, 255), randrange(1, 255), 5, 5))

        assert neuron.n_id == n_id

    def test_network_create(self):
        cr_id = 42
        network_size = 2
        network = Network(cr_id, network_size)

        self.assertEqual(network.n_id,cr_id)

