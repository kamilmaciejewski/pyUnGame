import pygame

import ung_globals
from engine.consoleHandler import ConsoleHandler
from engine.thread import ThreadWithException
from world.world import World
from slider import VerticalSlider

class GraphicsEngine(ThreadWithException):
    font = pygame.font
    screen = pygame.display
    world = World
    consoleHandler = ConsoleHandler
    sliders = []

    def __init__(self, name: str, world: World, fps: int, console: ConsoleHandler):
        super().__init__(name, fps)
        self.font = pygame.font.SysFont(ung_globals.font, ung_globals.fontSize)
        # pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode(ung_globals.screenSize)
        # , depth=32, flags=pygame.SRCALPHA)
        self.world = world
        self.consoleHandler = console
        self.sliders = [
        VerticalSlider(80, 80, 15, 200, name="A", min_val=0, max_val=100, initial=50, step=1),
        VerticalSlider(180, 80, 20, 200, name="B", min_val=0, max_val=100, initial=25, step=1),
        VerticalSlider(280, 80, 25, 200, name="C", min_val=0, max_val=100, initial=75, step=1),
        ]

    def run_loop(self):
        self.consoleHandler.put_permanent_msg("graphics engine", str(self.get_fps()))
        self.screen.fill((0, 0, 0, 128))
        self.consoleHandler.draw_console(self.screen, self.get_fps())
        for cr in self.world.creatures:
            cr.draw(self.screen)
        #for s in self.sliders:
            #s.draw(self.screen, self.font)
        pygame.display.flip()
