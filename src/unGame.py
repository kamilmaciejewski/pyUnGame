import sys
from random import randrange

import pygame

from src import logger
from src.creature import Creature
from src.engine.neuralEngine import NeuralEngine
from src.engine.worldEngine import WorldEngine
from src.world.world import World

sys.path.append('../')
# clock0 = pygame.time.Clock()


# def thread_function(args):
#     while True:
#
#         #print(len(args))
#         #for _ in range(1):
#         #    creatures.pop(0)
#
#         for creature in creatures:
#             creature.update()
#         global stop_threads
#         if stop_threads:
#             break
#         #time.sleep(2)
#         clock0.tick(500)


world = World()
for i in range(100):
    logger.log("unGame", " creature " + str(i) + " add")
    world.creatures.append(
        Creature(i, 350 + randrange(100), 250 + randrange(100), randrange(1, 10), randrange(5, 15), 1))

# stop_threads = False
# x = threading.Thread(target=thread_function, args=(creatures,))
# x.start()
pygame.init()
font = pygame.font.SysFont('lucidaconsole', 12)
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF, 32)
box = pygame.Rect(20, 20, 10, 10)
clock = pygame.time.Clock()
max_fps = 60

engines = []

worldEngine = WorldEngine(world, 'World engine', 10)
worldEngine.start()
engines.append(worldEngine)
neuralEngine = NeuralEngine(world, 'Neural engine', 10)
neuralEngine.start()
engines.append(neuralEngine)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for engine in engines:
                engine.raise_exception()
                engine.join()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            for engine in engines:
                engine.raise_exception()
                engine.join()
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

    screen.fill((0, 0, 0))
    offset = 25
    for engine in engines:
        screen.blit(font.render(str(engine.name) + ' ' + str(int(engine.get_fps())), True, pygame.Color('white')),
                    (5, offset))
        offset += 10
    world_size = font.render("World: " + str(len(world.creatures)), True, pygame.Color('white'))
    fps = font.render("Screen: " + str(int(clock.get_fps())), True, pygame.Color('white'))
    screen.blit(fps, (5, 5))
    screen.blit(world_size, (5, 15))

    stats = font.render("Stat: " + str(world.creatures[0].network.neurons[0].threshold), True, pygame.Color('white'))
    screen.blit(stats, (5, 50))
    stats0 = font.render("Neur count: " + str(world.creatures[0].network.counter), True, pygame.Color('white'))
    screen.blit(stats0, (5, 60))
    stats1 = font.render("Neur eng count: " + str(neuralEngine.counter), True,
                         pygame.Color('white'))
    screen.blit(stats1, (5, 70))

    for cr in world.creatures:
        pygame.draw.rect(screen, pygame.Color(50, 100, 200, 5), cr.body)

    pygame.draw.rect(screen, (0, 150, 255, 0), box)
    pygame.display.flip()
    clock.tick(max_fps)
