from abc import ABC, abstractmethod
from src.util.model_time import Time
from src.io import Driver


class Program(ABC):

    def __init__(self, driver: Driver):
        self.driver = driver

    @abstractmethod
    def run(self, tick: int, time: Time):
        pass
