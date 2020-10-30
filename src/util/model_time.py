REAL_SECONDS_PER_MODEL_SECOND = 2 / 60
MODEL_SECONDS_PER_TICK = 0.1
TICK_TIME = REAL_SECONDS_PER_MODEL_SECOND * MODEL_SECONDS_PER_TICK
print(TICK_TIME)

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
        self.second = int(model_second % 60)
        self.minute = int(model_minute % 60)
        self.hour = int(model_hour % 24)

    def get_tick(self) -> int:
        return ((self.hour*60+self.minute)*60+self.second) // MODEL_SECONDS_PER_TICK

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __eq__(self, other):
        return isinstance(other, Time) and \
               other.hour == self.hour and \
               other.minute == self.minute and \
               other.second == self.second

    def __lt__(self, other):
        return isinstance(other, Time) and \
               (self.hour < other.hour or
                self.hour == other.hour and self.minute < other.minute or
                self.hour == other.hour and self.minute == other.minute and self.second < other.second)
