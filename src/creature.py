from random import randrange

import pygame

from network import Network


class Creature(object):
    posX = 0.0
    posY = 0.0
    size = 10.0
    body = pygame.Rect(5, 5, 5, 5)
    network = Network(10)

    def __init__(self, pos_x, pos_y):
        self.posX = pos_x
        self.posY = pos_y
        self.body = pygame.Rect(pos_x, pos_y, self.size, self.size)

    def update(self):
        self.network.update()

    def shake(self):
        self.body.x += (randrange(-3, 4))
        self.body.y += (randrange(-3, 4))
