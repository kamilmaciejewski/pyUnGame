import os
import sys

import pygame

sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/..")
from engine.consoleHandler import ConsoleHandler



from engine.enginesHandler import EnginesHandler
from engine.graphicsEngine import GraphicsEngine
from engine.neuralEngine import NeuralEngine
from engine.worldEngine import WorldEngine
from world.world import World

#
# d = dict()
# d[0.7] = 42
# d[1.7] = 4
# od = collections.OrderedDict(sorted(d.items()))
#
# for k, v in od.items():
#     logger.log("ASD","K:" + str(k) + ",v:" + str(v))

pygame.init()
world = World()

box = pygame.Rect(20, 20, 10, 10)
enginesHandler = EnginesHandler()

consoleHandler = ConsoleHandler()

enginesHandler.add_engine(WorldEngine('World', world, 60, consoleHandler))
enginesHandler.add_engine(NeuralEngine('Neural', world, 60, consoleHandler))
enginesHandler.add_engine(GraphicsEngine('Graphics', world, 60, consoleHandler))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            found = False
            for cr in world.creatures:
                if cr.body.collidepoint(pos) and not found:
                    cr.is_active = True
                    found = True
                else:
                    cr.is_active = False

        if event.type == pygame.QUIT:
            enginesHandler.stop_all()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            enginesHandler.stop_all()
            sys.exit(0)

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

#   offset = 25
#    for engine in engines:
#        screen.blit(font.render(str(engine.name) + ' ' + str(int(engine.get_fps())), True, pygame.Color('white')),
#                    (5, offset))
#        offset += 10

#    world_size = font.render("World: " + str(len(world.creatures)), True, pygame.Color('white'))
#    fps = font.render("Screen: " + str(int(clock.get_fps())), True, pygame.Color('white'))
#    screen.blit(fps, (5, 5))
#    screen.blit(world_size, (5, 15))

#    stats = font.render("Stat: " + str(world.creatures[0].network.neurons[0].threshold), True, pygame.Color('white'))
#    screen.blit(stats, (5, 50))

#    pygame.draw.rect(screen, (0, 150, 255, 0), box)
#    clock.tick(max_fps)
