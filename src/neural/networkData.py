import numpy


class NetworkData:
    neurons_data = numpy.array
    neurons_data_res = numpy.array
    neurons_wages = numpy.array
    neurons_thresholds = numpy.array
    neurons_is_input = numpy.array

    def __init__(self, size: int):
        self.neurons_data = numpy.zeros(size)
        self.neurons_is_input = numpy.full(size, False)
        self.neurons_thresholds = numpy.full(size, 0.1)
        # self.neurons_thresholds_delta = numpy.full(size, 0.1)
        self.neurons_thresholds_delta = numpy.random.default_rng().uniform(0.005, 0.015, size)
        self.neurons_weights = numpy.zeros((size, size))
