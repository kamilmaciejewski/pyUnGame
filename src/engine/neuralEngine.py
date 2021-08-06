from src.creature import Creature
from src.engine.consoleHandler import ConsoleHandler
from src.engine.thread import ThreadWithException
from src.world.world import World


def lam(cr: Creature):
    # log("lam", "call" + str(cr.cr_id))
    return cr.network.update()


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

#        list(map(lam, self.world.creatures))
