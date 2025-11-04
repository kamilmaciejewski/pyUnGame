import pygame
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#from neuronConnection import NeuronConnection
import ung_globals
from typing import Tuple
import logging


class Neuron:
    val = 0
    connections = list #[NeuronConnection]
    threshold = float
    threshold_boost = float
    n_id = str
    body = pygame.Rect
    pos = tuple
    font = pygame.font
    shape_surf = pygame.Surface
    surface_size = 64
    
    

    def __init__(self, n_id: int, pos: tuple): #pos is actually 4 arguments, x, y size x, size y TODO: remove size from the params
        #self.font = pygame.font.SysFont(ung_globals.font, ung_globals.fontSize)
        self.n_id = n_id
        self.body = pygame.Rect(pos[0]-self.surface_size/2, pos[1]-self.surface_size/2, self.surface_size, self.surface_size)
        self.connections = list() #[NeuronConnection]
        self.threshold = 0
        self.pos = pos
        self.shape_surf = pygame.Surface(pygame.Rect(self.body).size, pygame.SRCALPHA) #for blending disabled neurons
        
        mean = 0.2
        std_dev = 0.02
        low, high = mean/2, 2*mean
        while True:
            x = random.gauss(mean, std_dev)
            if low <= x <= high:
                self.threshold_boost = x/10
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
        elif self.is_enabled(): #enabled, pump threshold
            self.threshold += self.threshold_boost
        else: #not enabled, lower threshold
            self.threshold -= (self.threshold_boost/10)
        return 0

    def add_connection(self, nc): #nc is NeuronConnection
        self.connections.append(nc)

    def is_enabled(self):
        return self.val >= self.threshold
    
    def midpoint(x1: int, x2: int) -> int:
        return round((x1 + x2) / 2)

    def connCol(weight): #float
        val = int(min(weight, 255))
        return pygame.Color(val, val, val)
    def draw(self, screen: pygame.surface):
        #for connection in self.connections:
            #pygame.draw.line(screen, connection.col, self.pos, connection.n.pos, 1)
            #valConn = self.font.render( f"w: {connection.weight:.2f}", True, pygame.Color('white'))
        
            #x = (self.body.centerx + connection.n.body.centerx) /2
            #y = (self.body.centery + connection.n.body.centery) /2
            #xy = (x , y)
            #screen.blit(valConn,(x,y))
        size = min(self.threshold*20,30)
        size2 = int(min(size*10, 255))
        if self.is_enabled():
            #pygame.draw.rect(screen, pygame.Color(0, 255, 0), self.body, 10, 5)
            pygame.draw.circle(screen, pygame.Color(0, 255, 0), self.pos, size)
        elif size2 > 30 :
            #alpha blend
            pygame.draw.circle(self.shape_surf, pygame.Color(255, 0, 0, size2), self.shape_surf.get_rect().center, size)
            screen.blit(self.shape_surf, self.body)
            #pygame.draw.circle(screen, pygame.Color(255, 0, 0, 64), self.pos, size)
        #val = self.font.render( f"v: {self.val:.2f}, th: {self.threshold:.2f}", True, pygame.Color('white'))
        #screen.blit(val,self.body) 
        