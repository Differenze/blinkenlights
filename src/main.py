import time
import threading
from flask import Flask, render_template, jsonify, request
# from multiprocessing import Process
import sys
from src.programs.flicker_on import FlickerOn
from src.programs.fire import Fire
from src.programs.simple_on_off import SimpleOnOff
from src.programs.broken_lamp import BrokenLamp
from src.programs.always_on import AlwaysOn
from src.util import model_time
from src.io.driver import Driver

app = Flask(__name__)
driver = Driver()

@app.route('/')
def hello_world():
    return render_template('index.js')


@app.route('/enable/<string:name>')
def enable(name):
    driver.set_light(name, 1)
    return ''

@app.route('/api/led_names')
def get_led_names():
    return jsonify(driver.address_dictionary)


@app.route('/api/post', methods=['POST'])
def post_test():
    led_name = request.form.get("name")
    led_value = float(request.form.get("value"))
    driver.set_light(led_name, led_value)
    return ''

@app.before_first_request
def init():
    initialize()




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
    AlwaysOn(driver, "inside_right", 0.8),
    AlwaysOn(driver, "inside_left", 1),
    # AlwaysOn(driver, "c"),
    # AlwaysOn(driver, "d"),
    # AlwaysOn(driver, "e"),
    # AlwaysOn(driver, "f"),
    # AlwaysOn(driver, "g"),
]


def program_thread(driver):
    SECONDS_PER_MODEL_SECOND = 0.1
    m_time = model_time.Time(18, 0, 0)
    # One loop per model second
    while True:
        m_time = m_time + model_time.Time(0, 0, 1)
        # print(m_time)
        for program in programs:
            program.run(m_time)
        # for i in range(0, 50):
        #     brightness = m_time.second/60+0.001
        #     driver.set_light_by_index(i, brightness)
        time.sleep(SECONDS_PER_MODEL_SECOND)





# if __name__ == "__main__":
def initialize():
    print("starting")
    for i in range(len(driver.brightness)):
        driver.set_light_by_index(0, 0)
    driver.start()
    pt = threading.Thread(target=program_thread, args=(driver,), daemon=True)
    pt.start()

    # time.sleep(100000)
    print("done")
