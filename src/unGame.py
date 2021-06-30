import logging
import threading
import time
from random import randrange

import pygame
import sys

from src.creature import Creature

creatures = []
clock0 = pygame.time.Clock()


def thread_function(args):
    while True:

        #print(len(args))
        #for _ in range(1):
        #    creatures.pop(0)

        for creature in creatures:
            creature.update()
        global stop_threads
        if stop_threads:
            break
        #time.sleep(2)
        clock0.tick(500)


for i in range(1000):
    # creature = Creature()
    creatures.append(Creature(350 + randrange(100), 250 + randrange(100)))

stop_threads = False
x = threading.Thread(target=thread_function, args=(creatures,))
x.start()
pygame.init()
logging.info("ASD")
font = pygame.font.Font(None, 20)
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF, 32)

# boxes = []


# boxes.append(pygame.Rect(20+randrange(700),20+randrange(500),10,10))

box = pygame.Rect(20, 20, 10, 10)

clock = pygame.time.Clock()

max_fps = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_threads = True
            x.join()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            stop_threads = True
            x.join()
            sys.exit(0)

    # delta += clock.tick()/1000.0
    # while delta > 1/max_tps:
    # delta -= 1/max_tps

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        box.x += 1
        thrStatus = False
    if keys[pygame.K_a]:
        box.x -= 1
    if keys[pygame.K_w]:
        box.y -= 1
    if keys[pygame.K_s]:
        box.y += 1

    screen.fill((0, 0, 0))
    fps = font.render("Screen: " + str(int(clock.get_fps())), True, pygame.Color('white'))
    fps0 = font.render("Engine: " + str(int(clock0.get_fps())), True, pygame.Color('white'))
    screen.blit(fps, (5, 5))
    screen.blit(fps0, (5, 20))

    for cr in creatures:
        cr.body.x += (randrange(-3, 4))
        cr.body.y += (randrange(-3, 4))
        pygame.draw.rect(screen, pygame.Color(50, 100, 200, 5), cr.body)

    pygame.draw.rect(screen, (0, 150, 255, 0), box)
    pygame.display.flip()
    clock.tick(max_fps)
