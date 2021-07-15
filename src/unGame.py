import sys
from random import randrange

import pygame

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
for i in range(300):
    # creature = Creature()
    world.creatures.append(Creature(350 + randrange(100), 250 + randrange(100)))

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

worldEngine = WorldEngine(world, 'World engine', 60)
worldEngine.start()
engines.append(worldEngine)
neuralEngine = NeuralEngine(world, 'Neural engine', 0)
neuralEngine.start()
engines.append(neuralEngine)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # stop_threads = True
            # x.join()
            worldEngine.raise_exception()
            worldEngine.join()
            neuralEngine.raise_exception()
            neuralEngine.join()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # stop_threads = True
            # x.join()
            worldEngine.raise_exception()
            worldEngine.join()
            neuralEngine.raise_exception()
            neuralEngine.join()
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
    offset = 100
    for engine in engines:
        # fpsEngine =
        screen.blit(font.render(str(engine.name) + ' ' + str(int(engine.get_fps())), True, pygame.Color('white')),
                    (5, offset))
        offset += 10
    fps = font.render("Screen: " + str(int(clock.get_fps())), True, pygame.Color('white'))
    # fps0 = font.render("Engine: " + str(int(clock0.get_fps())), True, pygame.Color('white'))
    world_size = font.render("World: " + str(len(world.creatures)), True, pygame.Color('white'))
    screen.blit(fps, (5, 5))

    # screen.blit(fps0, (5, 20))
    fps1 = font.render("World Engine: " + str(int(worldEngine.get_fps())), True, pygame.Color('white'))
    screen.blit(fps1, (5, 20))
    fps2 = font.render("Nural Engine: " + str(int(neuralEngine.get_fps())), True, pygame.Color('white'))
    screen.blit(fps2, (5, 30))
    screen.blit(world_size, (5, 35))

    for cr in world.creatures:
        pygame.draw.rect(screen, pygame.Color(50, 100, 200, 5), cr.body)

    pygame.draw.rect(screen, (0, 150, 255, 0), box)
    pygame.display.flip()
    clock.tick(max_fps)
