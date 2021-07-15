from src.engine.thread import ThreadWithException


class WorldEngine(ThreadWithException):
    world = None

    def __init__(self, world, name, fps):
        super().__init__(name, fps)
        self.world = world

    def run_loop(self):
        # time.sleep(1)
        for cr in self.world.creatures:
            cr.shake()
        # if len(self.world.creatures) > 0:
        # self.world.creatures.pop(0)
