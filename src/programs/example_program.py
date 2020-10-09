from .program import Program
from src.util.model_time import Time


class Example(Program):
    def run(self, tick: int, time: Time):
        if time.second > 30:
            self.driver
