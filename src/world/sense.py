from typing import List

import numpy

from src.utils import geometry
from src.world.food import Food


def scan(pos: tuple, food: Food):
    return geometry.calculate_distance(pos, food.body.center)


# Represents sense that can detect food (basing on distance between sensor pos and food pos)
# Init with array of True or False values. that represents input neurons distribution so we can math the results array.
# in: [True|False...]
# out: [0-1...]
class Sense(object):
    inputNeurons = numpy.array
    # values = numpy.array
    inputIdList = []

    # TODO: use direct write to network data handler (once done and tested)
    def __init__(self, input_neurons, neurons_is_input):
        self.inputNeurons = input_neurons
        self.inputNeurons = numpy.full(len(input_neurons), 0.)

        for i in range(len(neurons_is_input)):
            if neurons_is_input[i]:
                self.inputIdList.append(i)

    # TODO: for now input pos is not handled so all will have the same value. Fine for now, fix later.
    def update(self, pos: tuple, foods: List[Food]):

        self.inputNeurons.fill(0.)
        for food in foods:
            for value in self.inputIdList:
                self.inputNeurons[value] += scan(pos, food)

        return self.inputNeurons
