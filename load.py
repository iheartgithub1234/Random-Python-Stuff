import time

def load(word, symbol, amount, duration):
    print(word, end="", flush=True)
    for i in range(amount):
        time.sleep(duration)
        print(symbol, end="", flush=True)
    print()

load("Loading", ".", 3, 0.5)