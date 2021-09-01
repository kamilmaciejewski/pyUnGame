from src.neural.neuron import Neuron


class NeuronConnection:
    n = Neuron

    def __init__(self, n: Neuron):
        self.n = n
        # log("neuron", "Neuron connection " + str(self.weight) + " created")
