from abc import ABC, abstractmethod
from src.util.model_time import Time
from src.io.driver import Driver


class Program(ABC):

    def __init__(self, driver: Driver):
        self.driver = driver
        pass

    @abstractmethod
    def run(self, tick: int, time: Time):
        pass
