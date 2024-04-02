import itertools, time, threading

all_possibility = list(itertools.product(range(10), repeat=6))
stop_event = threading.Event()

def brute_force(test_cases_chunk, target_pin):
    for pin in test_cases_chunk:
        pin_str = ''.join(map(str, pin))
        # print(f"test: {pin_str}")
        if pin_str == target_pin:
            print(f"found: {pin_str}")
            stop_event.set()

def distribute_test_cases(num_threads, target_pin):
    chunk_size = len(all_possibility) // num_threads
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(all_possibility)
        test_cases_chunk = all_possibility[start:end] 
        thread = threading.Thread(target=brute_force, args=(test_cases_chunk, target_pin))
        threads.append(thread)
        thread.start()

    for thread in threads:
        if not stop_event.is_set():  # Periksa apakah event sudah di-set
            thread.join()

if __name__ == "__main__":
    target_pin = input("masukkan pin: ")
    num_threads = 4

    start = time.time()

    distribute_test_cases(num_threads, target_pin)

    # thread1 = threading.Thread(target=brute_force, args=(all_possibility[0:250000], target_pin))
    # thread1.start()
    # thread2 = threading.Thread(target=brute_force, args=(all_possibility[250000:50000], target_pin))
    # thread2.start()
    # thread3 = threading.Thread(target=brute_force, args=(all_possibility[50000:750000], target_pin))
    # thread3.start()
    # thread4 = threading.Thread(target=brute_force, args=(all_possibility[750000:1000000], target_pin))
    # thread4.start()

    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()

    end = time.time()
    print(f"time: {end - start}")
