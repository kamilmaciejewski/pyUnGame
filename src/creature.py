from random import randrange

import pygame

from network import Network
from src import logger


class Creature(object):
    posX = 0.0
    posY = 0.0
    size = 10.0
    speed = 5
    body = pygame.Rect
    network_size = 2
    network = Network
    cr_id = 0

    def __init__(self, cr_id, pos_x, pos_y, size, speed, network_size):
        logger.log("Creature", str(cr_id) + " created")
        self.cr_id = cr_id
        self.network = Network(cr_id, network_size)
        self.size = size
        self.posX = pos_x
        self.posY = pos_y
        self.body = pygame.Rect(pos_x - (self.size / 2), pos_y - (self.size / 2), self.size, self.size)
        self.speed = speed
        self.network_size = network_size

    def update(self):
        self.body.x += (randrange((-1 * self.speed) + 1, self.speed))
        self.body.y += (randrange((-1 * self.speed) + 1, self.speed))
