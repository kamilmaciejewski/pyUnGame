from src.neural.neuron import Neuron


class NeuronConnection:
    weight = int
    n = Neuron

    def __init__(self, n, w):
        self.n = n
        self.weight = w

    def calculate(self):
        return self.weight * self.n.val
