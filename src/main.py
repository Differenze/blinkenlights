import time
from src.programs.example_program import Example
from src.util import model_time

programs = [Example()]


def main_loop(tick):
    m_time.set_tick(tick)
    for program in programs:
        program.run(tick, m_time)
    print(m_time)
    pass


# Timing Loop
m_time = model_time.Time(0, 0, 0)
tick = m_time.get_tick()
start_time = time.time()
while True:
    tick += 1
    tick = (time.time()-start_time) // model_time.TICK_TIME
    main_loop(tick)
    time.sleep(model_time.TICK_TIME - ((time.time() - start_time) % model_time.TICK_TIME))
