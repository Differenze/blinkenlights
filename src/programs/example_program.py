
def init(x):
    print("example initialized", x)


def tick(timestamp: int):
    if timestamp % 1000 == 0:
        print("One second!")
