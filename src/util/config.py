import json


def load_file(filename):
    with open(filename) as cfile:
        config = json.load(cfile)
    return config


def get_address_dict():
    config = load_file("conf/config.json")
    registers = config["registers"]
    led_id = 0
    address_dictionary = dict()
    for register in registers:
        leds = register["leds"]
        for led in leds:
            address_dictionary[led] = led_id
            led_id += 1
    return address_dictionary
