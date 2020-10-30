from src.io.driver import Driver
from src.programs.program import Program
from src.util.model_time import Time


class AllaysOn(Program):
    def __init__(self, driver: Driver, led_name, brightness=9):
        super().__init__(driver)
        self.led_name = led_name
        self.brightness = brightness

    def run(self, tick: int, time: Time):
        self.driver.set_light(self.led_name, self.brightness)