from src.logger import log


class Neuron:
    val = 0
    connections = []
    threshold = 0
    threshold_boost = 0.001
    counter = 0

    def __init__(self):
        log("neuron", "Neuron created")

    def calculate(self):
        self.counter += 1
        self.val = 0
        for n in self.connections:
            self.val += n.n.is_enabled * n.weight
        if self.val > self.threshold:
            self.threshold += self.threshold_boost
        else:
            self.threshold -= self.threshold_boost

    def add_connection(self, nc):
        self.connections.append(nc)

    def is_enabled(self):
        return self.val >= self.threshold
