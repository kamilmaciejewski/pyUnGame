import ctypes
import threading

import pygame


class ThreadWithException(threading.Thread):
    clock = pygame.time.Clock()
    maxFps = 60
    previous = pygame.time.get_ticks()
    frameStart = pygame.time.get_ticks()
    frameSize = 0
    fps = 0
    tmpFps = 0

    def run_loop(self):
        pass

    def set_loop(self, runnable):
        self.run_loop = runnable

    def get_fps(self):
        # return self.clock.get_fps()
        return self.fps

    def run_base(self):
        while pygame.time.get_ticks() - self.frameStart < self.frameSize:
            pygame.time.wait(1)

        self.frameStart = pygame.time.get_ticks()

        if pygame.time.get_ticks() - self.previous < 1000:
            self.tmpFps += 1
        else:
            self.previous = pygame.time.get_ticks()
            self.frameStart = pygame.time.get_ticks()
            self.fps = self.tmpFps
            self.tmpFps = 0

        # self.clock.tick(self.maxFps)
        # self.previous = pygame.time.get_ticks()
        # pygame.time.wait(self.maxFps)

    def __init__(self, name, fps):
        threading.Thread.__init__(self)
        self.name = name + " " + str(fps)
        self.maxFps = fps
        if fps <= 0:
            return
        self.frameSize = 1000 / fps

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
