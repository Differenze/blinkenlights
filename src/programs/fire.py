from src.programs.program import Program
from src.util.model_time import Time
import random


def get_bits(number):
    ret = [0, 0]
    if number == 3:
        ret = [1, 1]
    if number == 2:
        ret = [1, 0]
    if number == 1:
        ret = [0, 1]
    return ret


class Fire(Program):

    def __init__(self, driver, r0, r1, y0, y1):
        Program.__init__(self, driver)
        self.r0 = r0
        self.r1 = r1
        self.y0 = y0
        self.y1 = y1

    def run(self, tick: int, time: Time):
        r = get_bits(random.randrange(1, 3))
        y = get_bits(random.randrange(1, 3))
        self.driver.set_light(self.r0, r[0])
        self.driver.set_light(self.r1, r[1])
        self.driver.set_light(self.y0, y[0])
        self.driver.set_light(self.y1, y[1])
        # self.driver.data[self.r0] = r[0]
        # self.driver.data[self.r1] = r[1]
        # self.driver.data[self.y0] = y[0]
        # self.driver.data[self.y1] = y[1]
        # self.driver.data[self.r0] = 0
        # self.driver.data[self.r1] = 0
        # self.driver.data[self.y0] = 0
        # self.driver.data[self.y1] = 1
