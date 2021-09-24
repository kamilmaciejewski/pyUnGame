import pygame


class Food(object):
    size = 10.0
    body = pygame.Rect
    f_id = 0
    energy = int
    shape_surf = pygame.Surface

    def __init__(self, f_id: int, pos_x, pos_y, size):
        self.energy = 2550000
        self.f_id = f_id
        self.size = size
        self.body = pygame.Rect(pos_x - (self.size / 2), pos_y - (self.size / 2), self.size, self.size)
        self.shape_surf = pygame.Surface(pygame.Rect(self.body).size, pygame.SRCALPHA)
        pygame.draw.rect(self.shape_surf, pygame.Color(0, 255, 0, 64), self.shape_surf.get_rect())

    # def update(self):

    def draw(self, screen):
        screen.blit(self.shape_surf, self.body)
        # pygame.draw.rect(screen, pygame.Color(255, 0, 0, 5), self.body, 2)

    def is_alive(self):
        return self.energy >= 0
