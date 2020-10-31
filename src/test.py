import RPi.GPIO as GPIO
import time

shift = 2
store = 3
data1 = 4

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(shift, GPIO.OUT)
# GPIO.setup(store, GPIO.OUT)
# GPIO.setup(data1, GPIO.OUT)
# GPIO.output(shift, GPIO.LOW)
# GPIO.output(store, GPIO.LOW)
# GPIO.output(data1, GPIO.LOW)

# GPIO.output(data1, 1)
# GPIO.output(shift, 1)
# GPIO.output(store, 1)

# GPIO.output(data1, 1)
# input("a")
# GPIO.output(shift, 1)
# input("b")
# GPIO.output(shift, 0)
# input("c")
# GPIO.output(data1, 0)
# input("d")
# GPIO.output(store, 1)
# input("e")
# GPIO.output(store, 0)
from src.io.driver import Driver

dr = Driver()
# dr.update_lights()
# dr.data = [0, 0, 0, 0, 0, 0, 0, 0]
# dr.data = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
           # 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
           # 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0
           # ]
# dr.data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# dr.data = [0, 1]
# dr.data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dr.update_lights(0)
cycle = [
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]]

i = 0
dr.start()
while True:
    input(dr.brightness)
    # dr.data = dr.data[1:len(dr.data)] + [dr.data[0]]
    # # dr.data[0:2] = cycle[i]
    # # dr.data[2:4] = cycle[i]
    # # dr.data[4:6] = cycle[i]
    # dr.data[6:8] = cycle[i]
    dr.set_light_by_index(i, 0.5)
    # dr.data = cycle[i]
    # i = (i+1) % len(cycle)
    i = (i+1) % 24

    dr.update_lights(0)
# # while True:
# #     for a in [0, 1]:
# #         for b in [0,1]:
# #             for c in [0,1]:
# #                 for d in [0, 1]:
# #                     x = [a, b, c, d]
# #                     input("test" + str(x))
# #                     dr.data[28:32] = x
# #                     # print(dr.data)
# #                     # dr.data[29:31] = y
# #                     dr.update_lights()