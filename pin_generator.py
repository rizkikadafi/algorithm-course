import random, hashlib

def gen():
    pin = ""
    for _ in range(6):
        pin += str(random.randint(0, 9))
    return pin

def hash_pin(pin):
    hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
    return hashed_pin


pin = input()
if pin == "":
    pin = gen()

print(hash_pin(pin))
print(pin)
