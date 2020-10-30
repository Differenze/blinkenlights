from .program import Program
from src.util.model_time import Time
import random

class Example(Program):
    bit = 30
    bit2 = 29
    goal = 0
    lasttick = 0

    def run(self, tick: int, time: Time):
        if tick-self.lasttick > 1:
            print("missed ticks: " + str(tick-self.lasttick))
        self.lasttick = tick

        if int(tick) % 7 == 1:
            self.driver.data[self.bit2] = 1
        else:
            self.driver.data[self.bit2] = 0
        self.driver.data[self.bit] = 1
        # if self.driver.data[self.bit] == 1:
        #     self.driver.data[self.bit] = 0
        # else:
        #     self.driver.data[self.bit] = 1
