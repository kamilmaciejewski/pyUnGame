import numpy


class NetworkData:
    neurons_data = numpy.array
    neurons_data_res = numpy.array
    neurons_wages = numpy.array
    neurons_thresholds = numpy.array
    neurons_is_input = numpy.array

    def __init__(self, size: int):
        self.neurons_data = numpy.zeros(size)
        self.neurons_is_input = numpy.full(size, 0)
        self.neurons_thresholds = numpy.full(size, 0.5)
        self.neurons_thresholds_delta = numpy.full(size, 0.01)
        self.neurons_weights = numpy.zeros((size, size))
