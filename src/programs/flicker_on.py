from src.io.driver import Driver
from src.programs.program import Program
from src.util.model_time import Time

pattern = [1, 0, 1]

class FlickerOn(Program):

    def __init__(self, driver: Driver, led: str, start_time):
        super().__init__(driver)
        self.led = led
        self.start_time = start_time
        self.enabled = False
        self.start_tick = 0

    def run(self, time: Time):
        # self.driver.set_light(self.led, 1)
        if not self.enabled:
            if time > self.start_time:
                self.enabled = True
                self.start_tick = time.second+1
            return
        pattern_pos = int(time.second-self.start_tick)
        if pattern_pos < len(pattern):
            self.driver.set_light(self.led, pattern[pattern_pos])
        else:
            self.driver.set_light(self.led, 1)
