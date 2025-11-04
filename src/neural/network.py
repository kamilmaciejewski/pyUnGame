import collections
from random import normalvariate
from random import randrange

import ung_globals
from neural.neuron import *
from neural.neuronConnection import NeuronConnection
from src.neural.networkData import NetworkData
from src.neural.networkDataHandler import NetworkDataHandler
from utils import geometry
from typing import Tuple
import logging
from sys import stdout
import numpy


def lam(neuron: Neuron):
    return neuron.calculate()
def randPos():
    return int(random.gauss(ung_globals.networkGraphSize/2 ,ung_globals.networkGraphSize/6))

class Network:
    data = NetworkData
    neurons = list[Neuron]
    n_id = int
    size = int
    shape_surf = pygame.Surface
    shape_surf_base = pygame.Surface
    input_size = 5

    def __init__(self, n_id : int, size : int):
        logging.info("Network init start")
        self.data = NetworkData(size)
        self.n_id = n_id
        self.neurons: list[Neuron] = []
        self.size = size
        
        self.shape_surf_base = pygame.Surface((ung_globals.networkGraphSize, ung_globals.networkGraphSize), pygame.SRCALPHA) #sufrace base, connections will be drawn on it once for buffering
        self.shape_surf = pygame.Surface((ung_globals.networkGraphSize, ung_globals.networkGraphSize), pygame.SRCALPHA) #sufrace for neurons, will be updated every frame
       
        for i in range(size):
            self.neurons.append(
                Neuron(i,
                        NetworkDataHandler(i, self.data),
                        (
                            randrange(1, ung_globals.networkGraphSize),
                            randrange(1, ung_globals.networkGraphSize))))
            if i < self.input_size:
                self.make_input(i) 
        
        logging.info("\nFill neurons start")
        
        while self.neurons.__len__() < size:
            #generate random position
            n = Neuron(str(self.n_id) + ":" + str(len(self.neurons)), (randPos(), randPos()))
            if self.checkDistances(n):
                self.neurons.append(n)
                sys.stdout.write("\rNeuron fill " + str(len(self.neurons)) + " of " + str(size))
                sys.stdout.flush()  
                #logging.info("Neuron fill " + str(len(self.neurons)) + " of " + str(size))
            
            
            
            #logging.info("Fill neurons done: " + str(i))
        self.init_connetctions() #calculate neurons connections
        self.draw_connections(self.shape_surf_base) #draw connections on the base surface
        
        
        #pygame.draw.rect(self.shape_surf, pygame.Color(128, 128, 128), self.shape_surf.get_rect(), 1) //does this do anything?

    def checkDistances(self, n : Neuron) -> bool:
        for neuron in self.neurons:
            #logging.info("Distance check: " + str(geometry.calculate_distance(neuron.pos, n.pos)))
            if geometry.calculate_distance(neuron.pos, n.pos) < ung_globals.neuronDistance:
                return False
        return True
        
    def init_connetctions(self):
        logging.info("\nFill connections start")
        for neuron in self.neurons:
            #logging.info("Connections fill " + neuron.n_id)
            #sys.stdout.write("\rConnections fill " + neuron.n_id)
            sys.stdout.flush()  
            #init connections
            #logging.info("Prepared connections: " + str(neuron.n_id))
            connections = dict()
            neuron.connections.clear

            for neuron0 in self.neurons:
                #skip self
                if not id(neuron) == id(neuron0):
                    #calculate all connections based on distance
                    connections[geometry.calculate_distance(neuron0.pos, neuron.pos)] = neuron0
            sorted_connections = collections.OrderedDict(sorted(connections.items()))

            #select shortest connections based on predefined limit
            for k, v in sorted_connections.items():
                if len(neuron.connections) < ung_globals.neuronConnections:
                    neuron.connections.append(NeuronConnection(v, k))
                else:
                    break
    
    def draw_connections(self, screen: pygame.surface):
        for neuron in self.neurons:
            for connection in neuron.connections:
                pygame.draw.line(screen, connection.col, neuron.pos, connection.n.pos, 1)
                
    def draw(self, screen: pygame.surface):
        enabledCount = 1
        warmCount = 1
        thr = 0.0
        thrWarm = 0.0
        self.shape_surf.fill((0, 0, 0))
        self.shape_surf.blit(self.shape_surf_base, (0, 0))  # draw connections on the base surface
        for neuron in self.neurons:
            neuron.draw(self.shape_surf)
            thr += neuron.threshold
            if neuron.is_enabled():
                enabledCount += 1
            elif neuron.threshold*50 > 1:
                warmCount += 1
                thrWarm += neuron.threshold
            else:
                thrWarm += neuron.threshold
            
        screen.blit(self.shape_surf, (0, 100))
        thr = thr / ung_globals.creatureNeurons
        thrWarm = thrWarm / (ung_globals.creatureNeurons - enabledCount)
        sys.stdout.write(
        "\rEnabled: " + str(enabledCount)
        + "/" + str(ung_globals.creatureNeurons)
        + ", Warm: " + str(warmCount)
        + "/" + str(ung_globals.creatureNeurons)
        + ", avg thr: " + str(thr)
        + ", avg thr disabled: " + str(thrWarm)
        )

        sys.stdout.flush()
    #def update(self):
        #for neuron in self.neurons:
            #neuron.calculate()
        #return self.n_id
    
    
    def update(self):
        # for neuron in self.neurons:
        #    neuron.calculate()

        input_data = numpy.dot(self.data.neurons_data * self.data.neurons_is_input,
                               self.data.neurons_weights.T)  # get data from input
        is_enabled = (self.data.neurons_data > self.data.neurons_thresholds)

        non_input_data_base = self.data.neurons_data * numpy.invert(
            numpy.invert(self.data.neurons_is_input) * is_enabled)
        non_input_data = numpy.dot(non_input_data_base,
                                   self.data.neurons_weights.T)  # get data from non input (only if neuron is enabled)

        # self.data.neurons_data = self.data.neurons_data * self.data.neurons_is_input  # clean data for non input
        # self.data.neurons_data = self.data.neurons_data + input_data + non_input_data
        # self.data.neurons_data = numpy.apply_along_axis(neural.sigmoid, -1, self.data.neurons_data)  # sigmoid

        threshold_delta = self.data.neurons_thresholds_delta * numpy.invert(self.data.neurons_is_input)
        is_enabled = (self.data.neurons_data > self.data.neurons_thresholds)
        delta_enabled = threshold_delta * numpy.invert(is_enabled)
        delta_disabled = threshold_delta * is_enabled

        self.data.neurons_thresholds = self.data.neurons_thresholds - delta_enabled + delta_disabled

        # list(map(lam, self.neurons))
        # return self.n_id

    def set_input_data(self, data):
        self.data.neurons_data = self.data.neurons_data * numpy.invert(
            self.data.neurons_is_input)  # clean data for input
        self.data.neurons_data = self.data.neurons_data + data

    def make_input(self, n_id: int):
        self.data.neurons_is_input[n_id] = True
        self.data.neurons_weights[n_id].fill(0.)
        self.data.neurons_thresholds[n_id] = 0.
        for conn in self.neurons[n_id].connections:
            conn.weight = 0.