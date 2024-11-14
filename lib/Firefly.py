import tkinter as tk
from threading import Thread, Semaphore
from typing import override
from lib.Display import Bulb

class Firefly(Thread):
    id = 0
    c_instance = 0

    freq = 1.0
    bulb = None

    __obsrvs = dict()
    __lock = Semaphore(1)

    def __init__(self):
        Firefly.c_instance += 1
        self.id = Firefly.c_instance
        self.bulb = Bulb(id)
        super().__init__()

    @override
    def run(self):
        # TODO: Run two different threads: One for blinking and one for observation
        pass

    def sync(self, firefly_id, freq):
        self.__lock.acquire()
        # TODO: Implement synchronization logics

        self.__lock.release()

    def __blink(self, driver):
        self.__lock.acquire()
        self.bulb.turn_on(sec=0.5)
        driver.send(firefly=self)
        self.__lock.release()

    def __obsrv(self, driver):
        # TODO: Implement observation logics
        driver.listen(self)
