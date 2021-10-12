from random import randrange

import pygame

from src import ung_globals
from src.neural.network import Network
from src.world.sense import Sense


class Creature(object):
    size = 10.0
    speed = 0.1
    body = pygame.Rect
    network = Network
    sense = Sense
    cr_id = 0
    is_active = False
    shape_surf = pygame.Surface
    energy = int
    count = int

    def __init__(self, cr_id, pos_x, pos_y, size, speed, network_size):
        self.energy = 2550000
        self.cr_id = cr_id
        self.network = Network(cr_id, network_size)
        # TODO: neurons position should be handled better
        # TODO: network geometry size should be a field rather than global value
        self.sense = Sense(self.network.data.neurons_data, self.network.data.neurons_is_input, self.network.neurons,
                           ung_globals.network_geometry_size)
        self.size = size
        self.body = pygame.Rect(pos_x - (self.size / 2), pos_y - (self.size / 2), self.size, self.size)
        self.speed = speed
        self.shape_surf = pygame.Surface(pygame.Rect(self.body).size, pygame.SRCALPHA)
        pygame.draw.rect(self.shape_surf, pygame.Color(50, 100, 200, 64), self.shape_surf.get_rect())
        self.count = 0

    def update(self, food):
        self.count += 1
        if self.is_alive() and not self.is_active:
            self.body.x += (randrange((-1 * self.speed) + 1, self.speed))
            self.body.y += (randrange((-1 * self.speed) + 1, self.speed))
            self.energy -= self.speed

        self.network.set_input_data(self.sense.update(self.body.center, food))
        # if self.is_active:
        #    log("Neuron " + str(self.network.neurons[0].n_id), " val: " + str(self.network.neurons[0].val))
        #    log("Neuron " + str(self.network.neurons[0].n_id), " thr: " + str(self.network.neurons[0].threshold))

    def draw(self, screen):
        if not self.is_alive():
            return
        screen.blit(self.shape_surf, self.body)
        if self.is_active:
            pygame.draw.rect(screen, pygame.Color(255, 0, 0, 5), self.body, 2)
            self.network.draw(screen)
            self.sense.draw(screen)

    def is_alive(self):
        return self.energy >= 0
