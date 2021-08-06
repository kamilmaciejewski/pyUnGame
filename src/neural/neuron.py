import pygame


class Neuron:
    val = 0
    connections = list
    threshold = float
    threshold_boost = 0.01
    n_id = str
    body = pygame.Rect

    def __init__(self, n_id, pos: tuple):
        self.n_id = n_id
        self.body = pygame.Rect(pos)
        self.connections = list()
        self.threshold = 0

    def lam(self, conn):
        if conn.n.is_enabled():
            self.val += conn.weight
        return 0

    def calculate(self):
        # log("neur", "OK")
        self.val = 0
        # list(map(self.lam, self.connections))
        for conn in self.connections:
            if conn.n.is_enabled():
                self.val += conn.weight

        if self.threshold == 0:
            self.threshold = self.val
        elif self.is_enabled():
            self.threshold += self.threshold_boost
        else:
            self.threshold -= self.threshold_boost
        return 0

    def add_connection(self, nc):
        self.connections.append(nc)

    def is_enabled(self):
        return self.val >= self.threshold

    def draw(self, screen: pygame.surface):

        if self.is_enabled():
            pygame.draw.rect(screen, pygame.Color(0, 255, 0), self.body, 1)
        else:
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), self.body, 1)

        for connection in self.connections:
            pygame.draw.line(screen, pygame.Color(128, 128, 128), self.body.center, connection.n.body.center, 1)
