from src import logger
from src.engine.thread import ThreadWithException


class NeuralEngine(ThreadWithException):
    world = None
    counter = 0

    def __init__(self, world, name, fps):
        super().__init__(name, fps)
        self.world = world

    def run_loop(self):
        logger.log("Neural engine", " update")
        self.counter += 1
        for creature in self.world.creatures:
            creature.network.update()
    # else:
    #  print("empty")
