import random

from src.io.driver import Driver
from src.programs.program import Program
from src.util.model_time import Time


class BrokenLamp(Program):
    brightness = 0
    flicker = False
    index = 0
    # TODO experiment with other patterns
    pattern = [1, 1, 1, 0, 1, 0, 0, 1]

    # flicker-on pattern (halogen lamp effect)
    # pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #            0.1, 0, 0.1, 0, 0.2, 0.1, 0, 0.5, 1]

    def __init__(self, driver: Driver, led_name, on_time, off_time):
        super().__init__(driver)
        self.on_time = on_time
        self.off_time = off_time
        self.led_name = led_name

    def run(self, time: Time):
        if time.second % 10 != 0:
            return
        if self.off_time > time > self.on_time:
            if self.flicker:
                if self.index < len(self.pattern):
                    self.driver.set_light(self.led_name, self.pattern[self.index])
                    self.index += 1
                else:
                    print("end flicker")
                    self.flicker = False
            else:
                dice = random.randrange(1, 101)
                if dice > 98:
                    print("start flicker")
                    self.flicker = True
                    self.index = 0
                self.driver.set_light(self.led_name, 1)

        else:
            self.driver.set_light(self.led_name, 0)
