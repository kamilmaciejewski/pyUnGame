from random import randrange

from src import ung_globals
from src.creature import Creature
from src.engine.consoleHandler import ConsoleHandler
from src.engine.thread import ThreadWithException
from src.world.world import World


class WorldEngine(ThreadWithException):
    world = None
    nextId = int
    consoleHandler = ConsoleHandler

    def __init__(self, name: str, world: World, fps: int, cons: ConsoleHandler):
        super().__init__(name, fps)
        self.world = world
        self.nextId = 0
        self.consoleHandler = cons

    def run_loop(self):
        self.consoleHandler.put_permanent_msg("world engine", str(self.get_fps()))
        self.consoleHandler.put_permanent_msg("creatures", str(len(self.world.creatures)))
        if len(self.world.creatures) < ung_globals.worldSize:
            self.world.creatures.append(
                Creature(self.nextId, 350 + randrange(100), 250 + randrange(100), randrange(15, 30), randrange(2, 6),
                         ung_globals.creatureNeurons))
            self.nextId += 1
        for cr in self.world.creatures:
            cr.update()
            if not cr.is_alive():
                self.world.creatures.remove(cr)
