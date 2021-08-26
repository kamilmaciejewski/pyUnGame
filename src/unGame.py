import os
import sys

import pygame

from src.engine.consoleHandler import ConsoleHandler
from src.logger import log

sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/..")

import time
from src.engine.enginesHandler import EnginesHandler
from src.engine.graphicsEngine import GraphicsEngine
from src.engine.neuralEngine import NeuralEngine
from src.engine.worldEngine import WorldEngine
from src.world.world import World

start = time.time()
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
enginesHandler.add_engine(GraphicsEngine('Graphics', world, 60, consoleHandler))
enginesHandler.add_engine(WorldEngine('World', world, 60, consoleHandler))
enginesHandler.add_engine(NeuralEngine('Neural', world, 999, consoleHandler))

while True:
    end = time.time()
    val = end - start
    days = val // 86400
    hours = val // 3600 % 24
    minutes = val // 60 % 60
    seconds = val % 60
    consoleHandler.put_permanent_msg("elapsed", str(int(days)) + "d, " + str(int(hours))+ "h, " + str(int(minutes)) + "m, " + str(int(seconds)) + "s")
    pygame.time.wait(1000)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            found = False
            for cr in world.creatures:
                if cr.body.collidepoint(pos) and not found:

                    cr.is_active = True
                    log("Data", str(cr.network.data.neurons_data))
                    log("Data_res", str(cr.network.data.neurons_data_res))
                    log("Weights", str(cr.network.data.neurons_weights[0]))
                    log("Conn", cr.network.neurons[0].get_conn_list())
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
