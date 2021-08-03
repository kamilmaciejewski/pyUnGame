import math
import random
from time import sleep

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

# target = (126, 270)
# start = (234, 54)
target = (random.randrange(600), random.randrange(600))
start = (random.randrange(600), random.randrange(600))
BLACK = (0, 0, 0)
BLUE = (0, 0, 128)
GREEN = (0, 128, 0)

pygame.draw.circle(screen, GREEN, start, 15)
pygame.draw.circle(screen, BLUE, target, 15)
pygame.draw.line(screen, BLUE, start, target, 5)
route = pygame.Surface((79, 1080))
route.set_colorkey(BLACK)
# BMP = pygame.image.load('art/trade_route00.png').convert()
(bx, by, bwidth, bheight) = route.get_rect()
# route.blit(BMP, (0,0), area=route.get_rect())
# get distance within screen in pixels
dist = math.sqrt((start[0] - target[0]) ** 2 + (start[1] - target[1]) ** 2)
# scale to fit: use distance between points, and make width extra skinny.
route = pygame.transform.scale(route, (int(bwidth * dist / bwidth * 0.05), int(bheight * dist / bheight)))
# and rotate... (invert, as negative is for clockwise)
angle = math.degrees(math.atan2(-1 * (target[1] - start[1]), target[0] - start[0]))
route = pygame.transform.rotate(route, angle + 90)
position = route.get_rect()
HERE = (abs(target[0] - position[2]), target[1])  # - position[3]/2)
print(HERE)
# screen.blit(route, HERE)
pygame.display.update()
sleep(1000)
print(start, target, dist, angle, position)
