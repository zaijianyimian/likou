import random
def rand16():
    return random.randint(0,65535)
def rand3000000():
    RANGE = 300000
    max_valid = 2**32
    while True:
        num = (rand16() << 16) | rand16()
        if num < max_valid:
            return num % RANGE
if __name__ == "__main__":
    for _ in range(5):
        print(rand3000000())