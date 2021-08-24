import unittest
from random import randrange

from src.neural.network import Network
from src.neural.neuron import Neuron


def print_network(network):
    print("Data:")
    print(network.neurons_data)
    print("Weights")
    print(network.neurons_weights)

    for neuron in network.neurons:
        print("neuron: " + str(neuron.n_id) + ", val: " + str(neuron.val) + ", thr: "
              + str(neuron.data_handler.get_threshold()))
        print("neuron: " + str(neuron.n_id) + ", is_enabled: " + str(neuron.is_enabled()))
        for conn in neuron.connections:
            print("conn: " + str(conn.n.n_id) + ": " + str(conn.weight))


class TestNeuralNetwork(unittest.TestCase):
    def test_neuron_create(self):
        size = 3
        n_id = 42
        # neurons_data = numpy.random.rand(size)
        # neurons_weights = numpy.zeros((size, size))
        #
        neuron = Neuron(n_id, None, (randrange(1, 255), randrange(1, 255), 5, 5))
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

    def test_network_input_calc(self):
        cr_id = 42
        network_size = 3
        network = Network(cr_id, network_size)

        print("\n\n=====Before=====\n")
        print_network(network)
        self.check_network(network)
        input_id = 1
        output_id = 2
        input_value = 0.88
        input_weight = 0.77
        self.assertEqual(False, network.neurons_is_input[input_id])
        network.make_input(input_id)
        self.assertEqual(True, network.neurons_is_input[input_id])

        network.update()
        print("\n=====After empty update=====\n")
        print_network(network)
        self.check_network(network)

        network.neurons_data[input_id] = input_value
        network.neurons_weights[output_id][input_id] = input_weight
        network.update()
        print("\n=====After update with vales=====\n")
        self.assertEqual(network.neurons_data_res[output_id], input_value * input_weight)
        self.assertEqual(network.neurons_data_res[input_id], 0.)
        print_network(network)

    def check_network(self, network):

        for neuron in network.neurons:
            self.assertEqual(neuron.val, network.neurons_data_res[neuron.n_id])

            if network.neurons_is_input[neuron.n_id]:
                self.assertEqual(0.0, network.neurons_thresholds[neuron.n_id])
            else:
                self.assertEqual(0.5, network.neurons_thresholds[neuron.n_id])
            for conn in neuron.connections:
                self.assertEqual(conn.weight, network.neurons_weights[neuron.n_id, conn.n.n_id])
