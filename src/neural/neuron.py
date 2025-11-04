import pygame
import random
import ung_globals
from typing import Tuple


class Neuron:
    val = 0
    connections = list
    threshold = float
    threshold_boost = float
    n_id = str
    body = pygame.Rect
    font = pygame.font
    

    def __init__(self, n_id, pos: tuple):
        self.font = pygame.font.SysFont(ung_globals.font, ung_globals.fontSize)
        self.n_id = n_id
        self.body = pygame.Rect(pos)
        self.connections = list()
        self.threshold = 0
        
        mean = 0.1
        std_dev = 0.02
        low, high = 0.01, 0.2
        while True:
            x = random.gauss(mean, std_dev)
            if low <= x <= high:
                self.threshold_boost = x
                #logging.info("threshold_boost: " + str(x))
                break


    def lam(self, conn): #is this even used?
        if conn.n.is_enabled(): #if the connected neuron is activated
            self.val += conn.weight #add the connection weight to value
        return 0

    def calculate(self):
        # log("neur", "OK")
        self.val = 0
        # list(map(self.lam, self.connections))
        for conn in self.connections:
            if conn.n.is_enabled(): #if the connected neuron is activated
                self.val += conn.weight #add the connection weight to value

        #TODO: remove this check, should not occur after first calculation, so could be moved to init
        if self.threshold == 0:
            self.threshold = self.val
        elif self.is_enabled():
            self.threshold += self.threshold_boost
        else:
            self.threshold -= (self.threshold_boost/20)
        return 0

    def add_connection(self, nc): #nc is NeuronConnection
        self.connections.append(nc)

    def is_enabled(self):
        return self.val >= self.threshold
    
    def midpoint(x1: int, x2: int) -> int:
        return round((x1 + x2) / 2)

    def draw(self, screen: pygame.surface):

        if self.is_enabled():
            pygame.draw.rect(screen, pygame.Color(0, 255, 0), self.body, 1)
        else:
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), self.body, 1)

        for connection in self.connections:
            pygame.draw.line(screen, pygame.Color(128, 128, 128), self.body.center, connection.n.body.center, 1)
            val = self.font.render(str(connection.weight), True, pygame.Color('white'))
            #x = self.midpoint(self.body.centerx, connection.n.body.centerx)
            x = (self.body.centerx + connection.n.body.centerx) /2
            y = (self.body.centery + connection.n.body.centery) /2
            xy = (x , y)
            screen.blit(val,xy)
