import itertools

all_possibility = list(itertools.product(range(10), repeat=6))
print("[")
for i in all_possibility:
    print(f"{i}, ")
print("]")
