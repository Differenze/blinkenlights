import time
import threading
import sys
from src.programs.flicker_on import FlickerOn
from src.programs.fire import Fire
from src.programs.simple_on_off import SimpleOnOff
from src.programs.broken_lamp import BrokenLamp
from src.programs.always_on import AlwaysOn
from src.util import model_time
from src.io.driver import Driver

driver = Driver()
programs = [
    # FlickerOn(driver, "inside_right", model_time.Time(18, 2, 0)),
    # FlickerOn(driver, "inside_left", model_time.Time(18, 2, 30)),
    # SimpleOnOff(driver, "street_light", model_time.Time(18, 5, 0), model_time.Time(23, 10, 0)),
    # BrokenLamp(driver, "outside_left", model_time.Time(18, 2, 0), model_time.Time(22, 0, 0)),
    # BrokenLamp(driver, "outside_middle", model_time.Time(18, 2, 0), model_time.Time(22, 0, 0)),
    # BrokenLamp(driver, "outside_right", model_time.Time(18, 2, 0), model_time.Time(22, 0, 0)),

    # SimpleOnOff(driver, "outside_middle", model_time.Time(18, 4, 0), model_time.Time(22, 0, 0)),
    # SimpleOnOff(driver, "outside_right", model_time.Time(18, 4, 0), model_time.Time(22, 0, 0)),
    # SimpleOnOff(driver, "cafe_entry", model_time.Time(18, 3, 0), model_time.Time(22, 10, 0)),

    # Fire(driver, "f2ya", "f2yb", "f2ra", "f2rb"),
    # AllaysOn(driver, "f2ya"),
    # AlwaysOn(driver, "a"),
    # AlwaysOn(driver, "b"),
]


def program_thread(driver):
    MILLISECONDS_PER_MODEL_SECOND = 0.1
    m_time = model_time.Time(18, 0, 0)
    # One loop per model second
    while True:
        m_time = m_time + model_time.Time(0, 0, 1)
        print(m_time)
        for program in programs:
            program.run(m_time)
        for i in range(0, 100):
            brightness = m_time.second/60+0.001
            driver.set_light_by_index(i, brightness)
        if brightness == 0:
            print("brightness")
        # print(brightness)
        # driver.set_light("outside_middle", brightness)
        time.sleep(MILLISECONDS_PER_MODEL_SECOND)


def driver_thread(driver):
    TICK_TIME = 0.003
    print("driver thread started")
    tick = 0
    start_time = time.time()
    missed_ticks = 0
    while True:
        last_tick = tick
        tick = (time.time() - start_time) // TICK_TIME
        if tick > last_tick + 1:
            missed_ticks += tick - (last_tick + 1)
            print("missed ticks ", missed_ticks)
        driver.update_lights(tick)
        time.sleep(TICK_TIME - ((time.time() - start_time) % TICK_TIME))


if __name__ == "__main__":
    driver = Driver()
    pt = threading.Thread(target=program_thread, args=(driver,), daemon=True)
    dt = threading.Thread(target=driver_thread, args=(driver,), daemon=True)
    pt.start()
    dt.start()
    time.sleep(100)
    print("done")
