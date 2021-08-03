from src.engine.consoleHandler import ConsoleHandler
from src.engine.thread import ThreadWithException
from src.world.world import World


class NeuralEngine(ThreadWithException):
    world = World
    consoleHandler = ConsoleHandler

    def __init__(self, name: str, world: World, fps: int, cons: ConsoleHandler):
        super().__init__(name, fps)
        self.world = world
        self.consoleHandler = cons

    def run_loop(self):
        self.consoleHandler.put_permanent_msg("neural engine fps", str(self.get_fps()))
        for creature in self.world.creatures:
            creature.network.update()
