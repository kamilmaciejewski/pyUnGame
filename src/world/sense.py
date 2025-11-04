from typing import List

import numpy
import pygame

from src import ung_globals
from src.utils import geometry
from src.utils.neural import sigmoid
from src.world.food import Food


def scan(pos: tuple, food: Food):
    return geometry.calculate_distance(pos, food.body.center)


# Represents sense that can detect food (basing on distance between sensor pos and food pos)
# Init with array of True or False values. that represents input neurons distribution so we can math the results array.
# in: [True|False...]
# out: [0-1...]
def relative_pos_shift(main_pos: tuple, pos_shift: tuple):
    return main_pos[0] + pos_shift[0], main_pos[1] + pos_shift[1]


class Sense(object):
    inputNeurons: numpy.array
    # values = numpy.array
    inputIdList: []
    inputPosList: dict
    # TODO this is temporary for drawing
    pos: tuple

    # TODO: use direct write to network data handler (once done and tested)
    def __init__(self, input_neurons, neurons_is_input, neurons_pos, network_size):
        self.inputNeurons = input_neurons
        self.inputNeurons = numpy.full(len(input_neurons), 0.)
        self.inputIdList = []
        self.inputPosList = dict()
        for i in range(len(neurons_is_input)):
            if neurons_is_input[i]:
                self.inputIdList.append(i)
                self.inputPosList[i] = ((neurons_pos[i].body.center[0] - network_size / 2) / 10,
                                        (neurons_pos[i].body.center[1] - network_size / 2) / 10)
                # print("current iteration: ", str(i))
                # print("list size: ", len(self.inputPosList))
                # print("neuron: ", str(i), ", pos: ", str(neurons_pos[i].body.center))
                # print("network_size/2: ", str(network_size / 2))
                # print("relative X: ", str((neurons_pos[i].body.center[0] - network_size) / 10))
                # print("relative Y: ", str((neurons_pos[i].body.center[1] - network_size) / 10))
                # print("relative position: ", str(self.inputPosList[i]))

    # TODO: for now input pos is not handled so all will have the same value. Fine for now, fix later.
    def update(self, pos: tuple, foods: List[Food]):
        self.pos = pos
        self.inputNeurons.fill(0.)
        for food in foods:
            for value in self.inputIdList:
                # self.inputNeurons[value] += (scan(relative_pos_shift(pos, self.inputPosList[value]), food))
                self.inputNeurons[value] += sigmoid(
                    1 - (scan(relative_pos_shift(pos, self.inputPosList[value]), food)) / 64)

        return self.inputNeurons

    def draw(self, screen):
        for value in self.inputIdList:
            tmpPos = relative_pos_shift((ung_globals.network_geometry_size / 2, ung_globals.network_geometry_size / 2),
                                        self.inputPosList[value])
            tmpRect = pygame.Rect(tmpPos[0], tmpPos[1], 10, 10)
            pygame.draw.rect(screen, pygame.Color(255, 0, 0, 5), tmpRect, 2)
