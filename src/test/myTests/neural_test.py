import unittest
from random import randrange

import numpy

from src.neural.network import Network
from src.neural.neuron import Neuron


def print_network(network):
    print("Data:")
    print(network.neurons_data)
    print("Weights")
    print(network.neurons_wages)

    for neuron in network.neurons:
        print("neuron: " + str(neuron.n_id) + ", val: " + str(neuron.val) + ", thr: " + str(neuron.threshold))
        print("neuron: " + str(neuron.n_id) + ", is_enabled: " + str(neuron.is_enabled()))
        for conn in neuron.connections:
            print("conn: " + str(conn.n.n_id) + ": " + str(conn.weight))


class TestNeuralNetwork(unittest.TestCase):
    def test_neuron_create(self):
        size = 3
        n_id = 42
        neurons_data = numpy.random.rand(size)
        neurons_wages = numpy.zeros((size, size))

        neuron = Neuron(n_id, neurons_data, neurons_wages, (randrange(1, 255), randrange(1, 255), 5, 5))
        self.assertEqual(neuron.n_id, n_id)

    def test_network_create(self):
        cr_id = 42
        network_size = 3
        network = Network(cr_id, network_size)

        print("\n\n=====Before=====\n")
        print_network(network)
        self.check_network(network)

        network.update()
        print("\n=====After=====\n")
        print_network(network)
        self.check_network(network)

    def check_network(self, network):

        for neuron in network.neurons:
            self.assertEqual(neuron.val, network.neurons_data_res[neuron.n_id])
            for conn in neuron.connections:
                self.assertEqual(conn.weight, network.neurons_wages[neuron.n_id, conn.n.n_id])
