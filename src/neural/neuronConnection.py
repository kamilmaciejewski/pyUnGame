from src.neural.neuron import Neuron


class NeuronConnection:
    weight = float
    n = Neuron

    def __init__(self, n: Neuron, w: float):
        self.n = n
        self.weight = w * 0.01
        # log("neuron", "Neuron connection " + str(self.weight) + " created")

    def calculate(self):
        return self.weight * self.n.val

