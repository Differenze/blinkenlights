import time
import threading
from src.io.driver import Driver
from src.util import model_time

global_variable = 0

def program_thread(driver):
    index = 0
    while True:
        index += 1
        print("working")
        brightness = (index % 10)/10
        driver.set_light("outside_middle", brightness)
        time.sleep(1)


def driver_thread():
    print("drivert started")
    m_time = model_time.Time(18, 0, 0)
    tick = m_time.get_tick()
    start_time = time.time() - tick * model_time.TICK_TIME
    driver.update_lights(0)
    missed_ticks = 0
    while True:
        last_tick = tick
        tick = (time.time() - start_time) // model_time.TICK_TIME
        if tick > last_tick + 1:
            missed_ticks += tick - (last_tick + 1)
            print("missed ticks ", missed_ticks)
        driver.update_lights(tick)
        time.sleep(model_time.TICK_TIME - ((time.time() - start_time) % model_time.TICK_TIME))


if __name__ == "__main__":
    driver = Driver()
    pt = threading.Thread(target=program_thread, daemon=True)
    dt = threading.Thread(target=driver_thread, daemon=True)
    pt.start()
    dt.start()
    time.sleep(10)

    print("done")
