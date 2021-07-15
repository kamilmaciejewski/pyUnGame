from src.logger import log


class Neuron:
    val = 0

    def __init__(self):
        log("neuron", "Neuron created")

    @staticmethod
    def calculate():
        val = 1
