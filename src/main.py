import time
MODEL_SECONDS_PER_REAL_SECOND = 2 / 60
MODEL_SECONDS_PER_TICK = 3
TICK_TIME = MODEL_SECONDS_PER_REAL_SECOND * MODEL_SECONDS_PER_TICK
print(TICK_TIME)


# 24hours = 86400 model seconds = 2880 seconds

# model seconds per tick = 5
# = 2/60*5 real seconds =

# 24 model hours -> 48 real minutes
# 1 model hour -> 2 real minutes
# 60 model minutes -> 120 real world seconds
# 1 model minute -> 2 real world seconds
# 1 model second -> 2 seconds / 60


def main_loop(tick):
    model_second = tick*MODEL_SECONDS_PER_TICK
    model_minute = model_second // 60
    model_hour = model_minute // 60
    print(time.time())
    print("{}:{}:{}".format(model_hour, model_minute, model_second))
    pass


tick = 0
start_time = time.time()
while True:
    tick += 1
    tick = (time.time()-start_time) // TICK_TIME
    main_loop(tick)
    # this_loop = time.time()
    # time.sleep(real_seconds_per_tick-(last_loop-this_loop))
    # last_loop = this_loop
    time.sleep(TICK_TIME - ((time.time() - start_time) % TICK_TIME))
