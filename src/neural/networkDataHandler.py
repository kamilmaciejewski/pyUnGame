from src.neural.networkData import NetworkData


class NetworkDataHandler:
    data = NetworkData
    neuron_id = int

    def __init__(self, n_id: int, n_data: NetworkData):
        self.neuron_id = n_id
        self.data = n_data

    def get_id(self) -> int:
        return self.neuron_id

    def get_val(self) -> float:
        return self.data.neurons_data[self.neuron_id]

    def get_threshold(self) -> float:
        return self.data.neurons_thresholds[self.neuron_id]

    def get_weights(self) -> float:
        return self.data.neurons_weights[self.neuron_id]

    def is_input(self) -> bool:
        return self.data.neurons_is_input[self.neuron_id]

    def set_input(self, value: float):
        if self.is_input():
            self.data.neurons_data = value
        else:
            raise Exception("Cannot set a non-input neuron")
