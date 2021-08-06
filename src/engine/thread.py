import ctypes
import threading

import pygame


class ThreadWithException(threading.Thread):
    clock = pygame.time.Clock

    def __init__(self, name, fps):
        self.clock = pygame.time.Clock()
        threading.Thread.__init__(self)
        self.name = name
        self.maxFps = fps

    def run_loop(self):
        pass

    def set_loop(self, runnable):
        self.run_loop = runnable

    def get_fps(self):
        return int(self.clock.get_fps())

    def run_base(self):
        self.clock.tick(self.maxFps)

    def run(self):

        # target function of the thread class
        try:
            while True:
                self.run_base()
                self.run_loop()
        finally:
            print('ended')

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def stop(self):
        self.raise_exception()
        self.join()

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

# t1 = ThreadWithException('Thread 1')
# t1.start()
# time.sleep(2)
# t1.raise_exception()
# t1.join()
