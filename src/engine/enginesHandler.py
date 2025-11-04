from engine.thread import ThreadWithException


class EnginesHandler:
    __engines = list

    def __init__(self):
        self.__engines = []

    def add_engine(self, engine: ThreadWithException):
        self.__engines.append(engine)
        engine.start()

    def stop_all(self):
        for engine in self.__engines:
            engine.stop()
