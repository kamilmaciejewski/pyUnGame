import pygame
from pygame.draw_py import Point

from src import ung_globals
from src.neural.networkDataHandler import NetworkDataHandler


def midpoint(p1, p2):
    return Point((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


class Neuron:
    # val = 0
    # connections = list
    # threshold_boost = 0.01
    n_id = int
    body = pygame.Rect
    data_handler = NetworkDataHandler

    def __init__(self, n_id, n_data_handler: NetworkDataHandler, pos: tuple):
        self.n_id = n_id
        self.body = pygame.Rect(pos)
        self.connections = list()
        self.data_handler = n_data_handler

    # def lam(self, conn):
    #     if conn.n.is_enabled():
    #         self.val += conn.weight
    #     return 0

    # def calculate(self):
    # log("neur", "OK")
    # self.val = 0
    # list(map(self.lam, self.connections))
    # for conn in self.connections:
    #    if conn.n.is_enabled():
    #        self.val += conn.weight
    # return 0

    def add_connection(self, nc):
        self.connections.append(nc)

    def is_enabled(self):
        return self.data_handler.get_val() >= self.data_handler.get_threshold()

    def get_val(self):
        return self.data_handler.get_val()

    def draw(self, screen: pygame.surface):

        if self.is_input():
            pygame.draw.rect(screen, pygame.Color(255, 255, 0), self.body, 1)
        elif self.is_enabled():
            pygame.draw.rect(screen, pygame.Color(0, 255, 0), self.body, 1)
        else:
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), self.body, 1)

        val = pygame.font.SysFont(ung_globals.font, ung_globals.neuron_fontSize).render(self.get_info(), True,
                                                                                        pygame.Color('white'))
        screen.blit(val, self.body.bottomright)
        for connection in self.connections:
            pygame.draw.line(screen, pygame.Color(128, 128, 128), self.body.center, connection.n.body.center, 1)
            # val = pygame.font.SysFont(ung_globals.font, ung_globals.neuron_fontSize).render(str(round(self.data_handler.get_weight(connection.n.n_id), 3)), True,
            #                                                                                 pygame.Color('white'))
            # screen.blit(val, midpoint(self.body.center, connection.n.body.center))

    def get_info(self) -> str:
        return str(self.n_id) + ": (" + str(round(self.get_val(), 2)) + ": " + str(
            round(self.data_handler.get_threshold(), 2)) + ")"

    def get_conn_list(self):
        res = ""
        for conn in self.connections:
            res += (str(conn.n.n_id) + ": " + str(conn.weight) + ";")
        return res

    def is_input(self):
        return self.data_handler.is_input()
