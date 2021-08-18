import numpy


class NetworkDataHandler:
    neurons_data = numpy.array
    neurons_data_res = numpy.array
    neurons_wages = numpy.array
    neurons_thresholds = numpy.array
    neurons_is_input = numpy.array
    neuron_id = int

    def __init__(self, n_id: int, n_data: numpy.array, n_data_res: numpy.array, n_data_weights: numpy.array,
                 n_data_thr: numpy.array, n_data_is_input: numpy.array):
        self.neuron_id = n_id
        self.neurons_data = n_data
        self.neurons_data_res = n_data_res
        self.neurons_weights = n_data_weights
        self.neurons_thresholds = n_data_thr
        self.neurons_is_input = n_data_is_input

    def get_id(self) -> int:
        return self.neuron_id

    def get_val(self) -> float:
        return self.neurons_data[self.neuron_id]

    def get_threshold(self) -> float:
        return self.neurons_thresholds[self.neuron_id]

    def get_weights(self) -> float:
        return self.neurons_weights[self.neuron_id]

    def is_input(self) -> bool:
        return self.neurons_is_input[self.neuron_id]

    def set_input(self, value: float):
        if self.is_input():
            self.neurons_data = value
        else:
            raise Exception("Cannot set a non-input neuron")
