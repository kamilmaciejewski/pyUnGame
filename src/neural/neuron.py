from src.logger import log


class Neuron:
    val = 0
    connections = []
    threshold = 0
    threshold_boost = 0.0001
    n_id = ""

    def __init__(self, n_id):
        self.n_id = n_id
        log("neuron", "Neuron " + self.n_id + " created")

    def calculate(self):
        log("neuron", self.n_id + " update")
        self.val = 0
        for n in self.connections:
            self.val += n.n.is_enabled * n.weight
        if self.val > self.threshold:
            if self.threshold >= 0.5:
                self.threshold += self.threshold_boost
            else:
                self.threshold -= self.threshold_boost
        else:
            if self.threshold <= 0.5:
                self.threshold += self.threshold_boost
            else:
                self.threshold -= self.threshold_boost

    def add_connection(self, nc):
        self.connections.append(nc)

    def is_enabled(self):
        return self.val >= self.threshold
