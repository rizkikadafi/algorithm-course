import itertools, time, threading

all_possibility = list(itertools.product(range(10), repeat=6))
event = threading.Event()

def brute_force(test_cases_chunk, target_pin, event: threading.Event, start_from_left = True):
    if start_from_left:
        for pin in test_cases_chunk:
            if event.is_set():
                return
            pin_str = ''.join(map(str, pin))
            # print(f"test: {pin_str}")
            if pin_str == target_pin:
                print(f"found: {pin_str}")
                event.set()
    else:
        for i in range(len(test_cases_chunk)-1, -1, -1):
            if event.is_set():
                return
            pin_str = ''.join(map(str, test_cases_chunk[i]))
            # print(f"test: {pin_str}")
            if pin_str == target_pin:
                print(f"found: {pin_str}")
                event.set()


def distribute_test_cases(num_threads, target_pin):
    chunk_size = len(all_possibility) // num_threads
    threads = []
    start_from_left = True

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(all_possibility)
        test_cases_chunk = all_possibility[start:end] 
        thread = threading.Thread(target=brute_force, args=(test_cases_chunk, target_pin, event, start_from_left))
        threads.append(thread)
        thread.start()
        start_from_left = not start_from_left

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_pin = input("masukkan pin: ")
    while len(target_pin) != 6 or not target_pin.isdecimal():
        print("panjang digit harus 6 dan harus angka")
        target_pin = input("masukkan pin: ")
    num_threads = 4

    start = time.time()

    distribute_test_cases(num_threads, target_pin)

    end = time.time()

    print(f"time: {end - start}")
