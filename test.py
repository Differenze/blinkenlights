import random
import time
import RPi.GPIO as GPIO
from collections import deque

GPIO.setmode(GPIO.BCM)

shift = 2
store = 3
data1 = 4
GPIO.setup(shift, GPIO.OUT)
GPIO.setup(store, GPIO.OUT)
GPIO.setup(data1, GPIO.OUT)
t = 0.5

GPIO.output(shift, GPIO.LOW)
GPIO.output(store, GPIO.LOW)
GPIO.output(data1, GPIO.LOW)

print("ready")

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
    "\"":[0, 0, 0, 1, 0, 0, 0, 0],
}

settle = 0.0001
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


light = True

anim = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
# anim = [
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
#     [0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],
# ]

data_array = [1,1,1,1,1,0,0,0]
# data_array = anim[0]
index = 0
delta = 1
# for i in range(0, 10):
#     set_lights(char_to_data[str(i)])
#     raw_input(i)

def get_bits_from_char(c):
    data = char_to_data["_"]
    if c.upper() in char_to_data:
        data = char_to_data[c.upper()]
    elif c.lower() in char_to_data:
        data = char_to_data[c.lower()]
    return data

            
text = "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."
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
    if (len(word) <= 4):
        write_4_letters(word + "   ")
    else:
        scroll_text(word)

delay = 0.5
write_word("    ")
# raw_input("go?")
# for word in text.split(" "):
#     write_word(word.strip(".").strip("?"))
#     time.sleep(delay/2)
#     write_word("    ")
#     time.sleep(delay)

# def bitfield(n):
#     return [int(digit) for digit in bin(n)[2:]]

def toBinary(number, size=8):
    res = []
    for i in range(size):
        x = number%2
        number = number//2
        res.insert(0, x)
    return res

for x in range(0, 8):
    for i in range(0, 8):
        print(toBinary(i, 4))
        set_lights(toBinary(i, 4))
        time.sleep(0.5)

while True:
    x = random.randrange(1, 8)
    set_lights(toBinary(x, 4))
    time.sleep(0.1)
set_lights([0,0,0,0])
# while True:
#     for a in range(0, 2):
#         for b in range(0, 2):
#             for c in range(0, 2):
#                 print(c, b, a)
#                 set_lights([c, b, a])
#                 raw_input(str(c)+str(b)+str(a))
