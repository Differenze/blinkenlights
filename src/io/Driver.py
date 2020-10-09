import random
import time
import RPi.GPIO as GPIO

# TODO read pins from config file

shift = 2
store = 3
data1 = 4
settle = 0.0001

# TODO read lookup table from file
char_to_data = {
            "0": [0, 1, 1, 1, 0, 1, 1, 1],
            "1": [0, 0, 0, 1, 0, 1, 0, 0],
            "2": [1, 0, 1, 1, 0, 0, 1, 1],
            "3": [1, 0, 1, 1, 0, 1, 1, 0],
            "4": [1, 1, 0, 1, 0, 1, 0, 0],
            "5": [1, 1, 1, 0, 0, 1, 1, 0],
            "6": [1, 1, 1, 0, 0, 1, 1, 1],
            "7": [0, 0, 1, 1, 0, 1, 0, 0],
            "8": [1, 1, 1, 1, 0, 1, 1, 1],
            "9": [1, 1, 1, 1, 0, 1, 1, 0],
            "A": [1, 1, 1, 1, 0, 1, 0, 1],
            "C": [0, 1, 1, 0, 0, 0, 1, 1],
            "E": [1, 1, 1, 0, 0, 0, 1, 1],
            "F": [1, 1, 1, 0, 0, 0, 0, 1],
            "G": [0, 1, 1, 0, 0, 1, 1, 1],
            "H": [1, 1, 0, 1, 0, 1, 0, 1],
            "I": [0, 1, 0, 0, 0, 0, 0, 1],
            "J": [0, 0, 0, 1, 0, 1, 1, 1],
            "K": [1, 0, 0, 1, 0, 1, 0, 0],
            "L": [0, 1, 0, 0, 0, 0, 1, 1],
            "M": [0, 0, 1, 0, 0, 1, 0, 1],
            "O": [0, 1, 1, 1, 0, 1, 1, 1],
            "P": [1, 1, 1, 1, 0, 0, 0, 1],
            "S": [1, 1, 1, 0, 0, 1, 1, 0],
            "U": [0, 1, 0, 1, 0, 1, 1, 1],
            "V": [0, 1, 0, 1, 0, 1, 1, 1],
            "W": [0, 1, 0, 1, 0, 0, 1, 0],
            "Z": [1, 0, 1, 1, 0, 0, 1, 1],
            "a": [1, 0, 1, 1, 0, 1, 1, 1],
            "b": [1, 1, 0, 0, 0, 1, 1, 1],
            "c": [1, 0, 0, 0, 0, 0, 1, 1],
            "d": [1, 0, 0, 1, 0, 1, 1, 1],
            "h": [1, 1, 0, 0, 0, 1, 0, 1],
            "n": [1, 0, 0, 0, 0, 1, 0, 1],
            "o": [1, 0, 0, 0, 0, 1, 1, 1],
            "q": [1, 1, 1, 1, 0, 1, 0, 0],
            "r": [1, 0, 0, 0, 0, 0, 0, 1],
            "t": [1, 1, 0, 0, 0, 0, 1, 1],
            "u": [0, 0, 0, 0, 0, 1, 1, 1],
            "y": [1, 1, 0, 1, 0, 1, 1, 0],
            "_": [0, 0, 0, 0, 0, 0, 1, 0],
            " ": [0, 0, 0, 0, 0, 0, 0, 0],
            "\"": [0, 0, 0, 1, 0, 0, 0, 0],
}


def initialize_driver():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(shift, GPIO.OUT)
    GPIO.setup(store, GPIO.OUT)
    GPIO.setup(data1, GPIO.OUT)
    GPIO.output(shift, GPIO.LOW)
    GPIO.output(store, GPIO.LOW)
    GPIO.output(data1, GPIO.LOW)
    print("ready")


def set_lights(data):
    GPIO.output(shift, GPIO.LOW)
    GPIO.output(store, GPIO.LOW)
    time.sleep(settle)
    for i in data:
        GPIO.output(data1, i)
        time.sleep(settle)
        GPIO.output(shift, GPIO.HIGH)
        time.sleep(settle)
        GPIO.output(shift, GPIO.LOW)
        time.sleep(settle)
    GPIO.output(store, GPIO.HIGH)
    time.sleep(settle)
    GPIO.output(store, GPIO.LOW)
    time.sleep(settle)


def get_bits_from_char(c):
    data = char_to_data["_"]
    if c.upper() in char_to_data:
        data = char_to_data[c.upper()]
    elif c.lower() in char_to_data:
        data = char_to_data[c.lower()]
    return data


def write_4_letters(string):
    data = []
    for i in range(0, 4):
        data += get_bits_from_char(string[i])
        print(data)
    set_lights(data)


def scroll_text(text):
    for letter in text:
        set_lights(get_bits_from_char(letter))
        time.sleep(0.2)


def write_word(word):
    if len(word) <= 4:
        write_4_letters(word + "   ")
    else:
        scroll_text(word)


def to_binary(number, size=8):
    res = []
    for i in range(size):
        x = number % 2
        number = number // 2
        res.insert(0, x)
    return res
