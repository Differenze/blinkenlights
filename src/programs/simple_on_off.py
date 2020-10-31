from src.io.driver import Driver
from src.programs.program import Program
from src.util.model_time import Time


class SimpleOnOff(Program):

    def __init__(self, driver: Driver, led_name, on_time, off_time):
        super().__init__(driver)
        self.on_time = on_time
        self.off_time = off_time
        self.led_name = led_name

    def run(self, time: Time):
        if self.off_time > time > self.on_time:
            self.driver.set_light(self.led_name, 1)
        else:
            self.driver.set_light(self.led_name, 0)
