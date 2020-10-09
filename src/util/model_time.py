MODEL_SECONDS_PER_REAL_SECOND = 2 / 60
MODEL_SECONDS_PER_TICK = 3
TICK_TIME = MODEL_SECONDS_PER_REAL_SECOND * MODEL_SECONDS_PER_TICK


class Time:
    hour = 0
    minute = 0
    second = 0

    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_tick(cls, tick: int):
        instance = cls(0, 0, 0)
        instance.set_tick(tick)
        return instance

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)

    def set_tick(self, tick: int):
        model_second = tick * MODEL_SECONDS_PER_TICK
        model_minute = model_second // 60
        model_hour = model_minute // 60
        self.second = model_second % 60
        self.minute = model_minute % 60
        self.hour = model_hour % 60

    def get_tick(self) -> int:
        return ((self.hour*24+self.minute)*60+self.second) // MODEL_SECONDS_PER_TICK

    def __str__(self):
        return "{}:{}:{}".format(self.hour, self.minute, self.second)

    def __eq__(self, other):
        return isinstance(other, Time) and \
               other.hour == self.hour and \
               other.minute == self.minute and \
               other.second == self.second
