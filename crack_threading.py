import itertools, hashlib, time, threading

all_possibility = list(itertools.product(range(10), repeat=6))
event = threading.Event()

def brute_force(test_cases_chunk, target_hash, event: threading.Event, start_from_left = True):
    if start_from_left:
        for pin in test_cases_chunk:
            if event.is_set():
                return
            pin_str = ''.join(map(str, pin))
            hashed_pin = hashlib.sha256(pin_str.encode()).hexdigest()
            # print(f"test: {hashed_pin}")
            if hashed_pin == target_hash:
                print(f"found: {pin_str}")
                event.set()
    else:
        for i in range(len(test_cases_chunk)-1, -1, -1):
            if event.is_set():
                return
            pin_str = ''.join(map(str, test_cases_chunk[i]))
            hashed_pin = hashlib.sha256(pin_str.encode()).hexdigest()
            # print(f"test: {hashed_pin}")
            if hashed_pin == target_hash:
                print(f"found: {pin_str}")
                event.set()

def distribute_test_cases(num_threads, target_hash):
    chunk_size = len(all_possibility) // num_threads
    threads = []
    start_from_left = True

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(all_possibility)
        test_cases_chunk = all_possibility[start:end] 
        thread = threading.Thread(target=brute_force, args=(test_cases_chunk, target_hash, event, start_from_left))
        threads.append(thread)
        thread.start()
        start_from_left = not start_from_left

    for thread in threads:
        thread.join()

f = open("pin.txt", "r")
target_hash = f.readline().strip()
# pin = f.read().strip()
f.close()

num_threads = 4
start = time.time()

distribute_test_cases(num_threads, target_hash)

end = time.time()
print(f"time: {end - start}")
