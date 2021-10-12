from random import randrange

from src import ung_globals
from src.engine.consoleHandler import ConsoleHandler
from src.engine.thread import ThreadWithException
from src.world.creature import Creature
from src.world.food import Food
from src.world.world import World


class WorldEngine(ThreadWithException):
    world = None
    nextId = int
    consoleHandler = ConsoleHandler
    counter = int

    def __init__(self, name: str, world: World, fps: int, cons: ConsoleHandler):
        super().__init__(name, fps)
        self.world = world
        self.nextId = 0
        self.consoleHandler = cons
        self.counter = 0
        self.world.food.append(
            Food(self.nextId, 350 + randrange(100), 250 + randrange(100), randrange(50, 100)))

    def run_loop(self):
        self.consoleHandler.put_permanent_msg("world engine", str(self.get_fps()))

        if len(self.world.creatures) < ung_globals.worldSize:
            self.consoleHandler.put_permanent_msg("creatures", str(len(self.world.creatures)))
            self.counter += 1
            self.consoleHandler.put_permanent_msg("cr ever sum", str(self.counter))
            self.consoleHandler.put_permanent_msg("neur sum",
                                                  str(format((self.counter * ung_globals.creatureNeurons), ",")))
            self.consoleHandler.put_permanent_msg("conn sum",
                                                  str(format((self.counter * ung_globals.creatureNeurons
                                                              * ung_globals.neuronConnections), ",")))
            self.world.creatures.append(
                Creature(self.nextId, randrange(1024), randrange(1024), randrange(15, 30), randrange(2, 6),
                         ung_globals.creatureNeurons))
            self.nextId += 1
            self.world.creatures[0].is_active = True
        for cr in self.world.creatures:
            cr.update(self.world.food)
            if not cr.is_alive():
                self.world.creatures.remove(cr)
