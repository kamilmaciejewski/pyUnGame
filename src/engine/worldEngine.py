from random import randrange

import ung_globals
from creature import Creature
from engine.consoleHandler import ConsoleHandler
from engine.thread import ThreadWithException
from world.world import World


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
            #self.consoleHandler.put_msg("creature add: " + str(self.nextId))
            self.world.creatures.append(
                Creature(
                    self.nextId,  #creature ID
                    350 + randrange(100), #position X
                    250 + randrange(100), #position Y
                    randrange(15, 30), #size
                    randrange(2, 6), #speed
                    ung_globals.creatureNeurons #network size
                    ))
            self.nextId += 1
            self.world.creatures[0].is_active = True
        for cr in self.world.creatures:
            cr.update(self.world.food)
            if not cr.is_alive():
                self.world.creatures.remove(cr)
