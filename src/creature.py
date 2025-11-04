from random import randrange

import pygame

from neural.network import Network


class Creature(object): #attributes and default values
    #constants
    body = pygame.Rect
    shape_surf = pygame.Surface
    #variables
    size = int
    speed = int
    network_size = int
    network = Network #each creature carries it's neural network as it's brain
    cr_id = int #id is updated on init
    is_active = False
    energy = int
    count = 0 #number of update cycles, like age

    def __init__(self, cr_id, pos_x, pos_y, size, speed, network_size):
        self.energy = 2550
        self.cr_id = cr_id
        self.network = Network(cr_id, network_size)
        self.size = size
        self.body = pygame.Rect(pos_x - (self.size / 2), pos_y - (self.size / 2), self.size, self.size)
        self.speed = speed
        self.network_size = network_size
        self.shape_surf = pygame.Surface(pygame.Rect(self.body).size, pygame.SRCALPHA)
        pygame.draw.rect(self.shape_surf, pygame.Color(50, 100, 200, 64), self.shape_surf.get_rect())
        #self.count = 0

    def update(self):
        self.count += 1
        if self.is_alive():
            self.body.x += (randrange((-1 * self.speed) + 1, self.speed))
            self.body.y += (randrange((-1 * self.speed) + 1, self.speed))
           #self.energy -= self.speed
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

    def is_alive(self):
        #return self.energy >= 0
        return True
