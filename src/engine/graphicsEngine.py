import pygame

import ung_globals
from engine.consoleHandler import ConsoleHandler
from engine.thread import ThreadWithException
from world.world import World


class GraphicsEngine(ThreadWithException):
    font = pygame.font
    screen = pygame.display
    world = World
    consoleHandler = ConsoleHandler

    def __init__(self, name: str, world: World, fps: int, console: ConsoleHandler):
        super().__init__(name, fps)
        self.font = pygame.font.SysFont(ung_globals.font, ung_globals.fontSize)
        # pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode(ung_globals.screenSize)
        # , depth=32, flags=pygame.SRCALPHA)
        self.world = world
        self.consoleHandler = console

    def run_loop(self):
        self.consoleHandler.put_permanent_msg("graphics engine", str(self.get_fps()))
        self.screen.fill((0, 0, 0, 128))
        self.consoleHandler.draw_console(self.screen, self.get_fps())
        for cr in self.world.creatures:
            cr.draw(self.screen)
        pygame.display.flip()
