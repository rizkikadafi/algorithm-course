import itertools, hashlib, time

def brute_force(target_hash):
    for pin in itertools.product(range(10), repeat=6):
        pin_str = ''.join(map(str, pin))
        hashed_pin = hashlib.sha256(pin_str.encode()).hexdigest()
        # print(f"test: {hashed_pin}")
        if hashed_pin == target_hash:
            print("found:")
            return ''.join(map(str,pin))

f = open("pin.txt", "r")
target_hash = f.readline().strip()
pin = f.read().strip()
f.close()

start = time.time()

print(brute_force(target_hash))

end = time.time()
print(f"time: {end - start}")
