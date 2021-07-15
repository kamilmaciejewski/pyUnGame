from src.engine.thread import ThreadWithException


class NeuralEngine(ThreadWithException):
    world = None

    def __init__(self, world, name, fps):
        super().__init__(name, fps)
        self.world = world

    def run_loop(self):
        for creature in self.world.creatures:
            creature.update()
    # else:
    #  print("empty")
