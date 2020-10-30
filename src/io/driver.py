import random
import time
import RPi.GPIO as GPIO
import src.util.config as config_loader

# TODO read pins from config file

shift = 2
store = 3
data1 = 4
# settle = 0.00000075
settle = 0.1

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


def set_lights(data):
    GPIO.output(shift, GPIO.LOW)
    GPIO.output(store, GPIO.LOW)
    for i in data.__reversed__():
        GPIO.output(data1, i)
        GPIO.output(shift, GPIO.HIGH)
        GPIO.output(shift, GPIO.LOW)
    GPIO.output(store, GPIO.HIGH)
    GPIO.output(store, GPIO.LOW)
    GPIO.output(data1, 0)


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


class Driver:
    data = []
    brightness = []

    def get_bits_from_char(self, char):
        return get_bits_from_char(char)

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(shift, GPIO.OUT)
        GPIO.setup(store, GPIO.OUT)
        GPIO.setup(data1, GPIO.OUT)
        GPIO.output(shift, GPIO.LOW)
        GPIO.output(store, GPIO.LOW)
        GPIO.output(data1, GPIO.LOW)
        self.address_dictionary = config_loader.get_address_dict()
        # print(self.address_dictionary)
        # self.data = [False for item in self.address_dictionary]
        # self.brightness = [0 for item in self.address_dictionary]
        self.data = [False for item in range(0, 100)]
        self.brightness = [0 for item in range(0, 100)]
        print("ready")

    def update_lights(self, tick):
        threshhold = (tick % 5) / 5
        for i in range(len(self.brightness)):
            self.data[i] = self.brightness[i] > threshhold
        set_lights(self.data)

    def set_light(self, name: str, brightness):
        if name not in self.address_dictionary:
            print("Could not find led with name: ", name)
        else:
            led_id = self.address_dictionary[name]
            self.brightness[led_id] = brightness

    def set_light_by_index(self, index, brightness):
        if index < 0 or index >= len(self.brightness):
            print("index out of range ", index)
        else:
            self.brightness[index] = brightness
