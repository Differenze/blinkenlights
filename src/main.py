import time
import sys
from src.programs.example_program import Example
from src.programs.flicker_on import FlickerOn
from src.programs.fire import Fire
from src.programs.simple_on_off import SimpleOnOff
from src.programs.broken_lamp import BrokenLamp
from src.programs.allways_on import AllaysOn
from src.util import model_time
from src.io.driver import Driver

driver = Driver()
programs = [
    # Example(driver),
    # FlickerOn(driver, "inside_right", model_time.Time(18, 2, 0)),
    # FlickerOn(driver, "inside_left", model_time.Time(18, 2, 30)),
    # SimpleOnOff(driver, "street_light", model_time.Time(18, 5, 0), model_time.Time(23, 10, 0)),
    # BrokenLamp(driver, "outside_left", model_time.Time(18, 2, 0), model_time.Time(22, 0, 0)),
    BrokenLamp(driver, "outside_middle", model_time.Time(18, 2, 0), model_time.Time(22, 0, 0)),
    # BrokenLamp(driver, "outside_right", model_time.Time(18, 2, 0), model_time.Time(22, 0, 0)),

    # SimpleOnOff(driver, "outside_middle", model_time.Time(18, 4, 0), model_time.Time(22, 0, 0)),
    # SimpleOnOff(driver, "outside_right", model_time.Time(18, 4, 0), model_time.Time(22, 0, 0)),
    # SimpleOnOff(driver, "cafe_entry", model_time.Time(18, 3, 0), model_time.Time(22, 10, 0)),

    # Fire(driver, "f2ya", "f2yb", "f2ra", "f2rb"),
    # AllaysOn(driver, "f2ya"),
    # AllaysOn(driver, "a")
]


def main_loop(tick):
    m_time.set_tick(tick)
    for program in programs:
        program.run(tick, m_time)
    if tick % 10 == 0:
        print(m_time)
    driver.update_lights(tick)


# Timing Loop
m_time = model_time.Time(18, 0, 0)
tick = m_time.get_tick()
start_time = time.time()-tick*model_time.TICK_TIME
driver.update_lights(0)
last_time = time.time()
missed_ticks = 0
while True:
    last_tick = tick
    tick = (time.time()-start_time) // model_time.TICK_TIME
    if tick > last_tick + 1:
        missed_ticks += tick - (last_tick + 1)
        print("missed ticks ", missed_ticks)
    main_loop(tick)
    time.sleep(model_time.TICK_TIME - ((time.time() - start_time) % model_time.TICK_TIME))
