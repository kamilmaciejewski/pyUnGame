import unittest
from random import randrange

import numpy as np

from src.neural.network import Network
from src.neural.neuron import Neuron


def print_network(network):
    print("Data:")
    print(network.data.neurons_data)
    print("Weights")
    print(network.data.neurons_weights)
    print("Threshold")
    print(network.data.neurons_thresholds)

    for neuron in network.neurons:
        print("neuron: " + str(neuron.n_id) + ", val: " + str(neuron.get_val()) + ", thr: "
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

    def test_network_empty_calc(self):
        cr_id = 42
        network_size = 3
        network = Network(cr_id, network_size)

        print("\n\n=====Before=====\n")
        print_network(network)
        self.check_network(network)

        network.update()
        print("\n=====After empty update=====\n")
        print_network(network)
        self.check_network(network)

    def test_network_data_handler(self):
        cr_id = 42
        network_size = 3
        network = Network(cr_id, network_size)

        print("\n\n=====Before=====\n")

        n_id = 0

        n_value = 0.88
        n_weight = 0.5
        n_threshold = 0.3
        network.data.neurons_data = network.data.neurons_data * 1
        network.data.neurons_data[n_id] = n_value
        print(network.data.neurons_data)
        print(network.neurons[0].data_handler.data.neurons_data)
        self.assertTrue(np.array_equal(network.data.neurons_data, network.neurons[0].data_handler.data.neurons_data))

        # network.update()

        print("network.neurons_data")
        print(network.data.neurons_data)

        print("network.neurons[0].data_handler.neurons_data")
        print(network.neurons[0].data_handler.data.neurons_data)
        print(np.array_equal(network.data.neurons_data, network.neurons[0].data_handler.data.neurons_data))

        self.assertTrue(np.array_equal(network.data.neurons_data, network.neurons[0].data_handler.data.neurons_data))

    def test_network_input_calc(self):
        cr_id = 42
        network_size = 3
        network = Network(cr_id, network_size)

        print("\n\n=====Before=====\n")

        input_id = 0
        output_id = 1
        input_value = 0.88
        input_weight = 0.5
        output_threshold = 0.55
        threshold_delta = 0.1
        self.assertEqual(False, network.data.neurons_is_input[input_id])
        network.make_input(input_id)
        self.assertEqual(True, network.data.neurons_is_input[input_id])

        print("Set input neuron: " + str(input_id) + " value: " + str(input_value))
        network.data.neurons_data[input_id] = input_value

        print("Set connection input: " + str(input_id) + " to output: " + str(output_id) + "value: "
              + str(input_weight))
        network.data.neurons_weights[output_id][input_id] = input_weight

        print("Set output neuron: " + str(output_id) + " threshold value: " + str(input_value))
        network.data.neurons_thresholds[output_id] = output_threshold
        network.data.neurons_thresholds_delta[output_id] = threshold_delta

        self.assertFalse(network.neurons[output_id].is_enabled(), "Expected neuron disabled")

        # self.assertEqual(network.neurons_data, network.neurons[output_id].data_handler.neurons_data,
        #                  "Data not the same")
        print_network(network)
        network.update()

        print("\n=====network.neurons_data=====\n")
        print(network.data.neurons_data)
        print("\n=====data_handler.neurons_data=====\n")
        print(network.neurons[output_id].data_handler.data.neurons_data)

        print("\n=====After update with vales=====\n")

        print_network(network)
        self.assertEqual(input_value, network.data.neurons_data[input_id], "Input should be the same as before update")
        self.assertEqual(input_value * input_weight, network.data.neurons_data[output_id],
                         "Expected output: input*weight")

        print("network.data.neurons_data")
        print(network.data.neurons_data)
        print("network.neurons[output_id].data_handler.data.neurons_data")
        print(network.neurons[output_id].data_handler.data.neurons_data)
        self.assertTrue(
            np.array_equal(network.data.neurons_data, network.neurons[output_id].data_handler.data.neurons_data),
            "Data not the same")

        self.assertEqual(input_value * input_weight, network.neurons[output_id].get_val(), "Expected value:" +
                         str(input_value * input_weight))
        # self.assertEqual(, network.neurons_thresholds, "Expected value:" +
        #                  str(input_value * input_weight))
        self.assertFalse(network.neurons[output_id].is_enabled(), "Expected output: DISABLED")
        self.assertEqual((output_threshold + threshold_delta), network.data.neurons_thresholds[output_id],
                         "Expected output: input*weight")

        print_network(network)

    def check_network(self, network):

        for neuron in network.neurons:
            self.assertEqual(neuron.get_val(), network.data.neurons_data[neuron.n_id])

            if network.data.neurons_is_input[neuron.n_id]:
                self.assertEqual(0.0, network.data.neurons_thresholds[neuron.n_id])
            # else:
            # self.assertEqual(0.5, network.data.neurons_thresholds[neuron.n_id])
            for conn in neuron.connections:
                self.assertEqual(conn.weight, network.data.neurons_weights[neuron.n_id, conn.n.n_id])
