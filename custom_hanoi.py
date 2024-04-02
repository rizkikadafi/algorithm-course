a = list(map(int, input("enter initial list: ").split()))
a_cpy = a.copy()
b = []
c = []
min_elm = min(a_cpy)
list_len = len(a)

print(f"initial condition: {a} | {b} | {c}")
src = a
target = c
count = 0
while True:
    if len(b) == list_len:
        break

    if len(target) != 0:
        if target[-1] == min_elm or len(src) == 0 or (src[-1] != min_elm and min_elm in target):
            src, target = target, src

    x = src.pop()
    if x != min_elm:
        target.append(x)
    else:
        b.append(x)
        a_cpy.remove(x)
        if len(a_cpy) > 0:
            min_elm = min(a_cpy)
    count += 1
    print(f"{a} | {b} | {c}")

print("the number of movement: ",count)

