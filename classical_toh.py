def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        # print(f"Move disk 1 from {source} to {target}")
        target.append(source.pop())
        print(a)
        print(b)
        print(c)
        print("-------------")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    # print(f"Move disk {n} from {source} to {target}")
    target.append(source.pop())
    print(a)
    print(b)
    print(c)
    print("-------------")
    tower_of_hanoi(n-1, auxiliary, target, source)

a = [3,2,1]
b = []
c = []
# print(a)
# print(b)
# print(c)
# print("-------------")
tower_of_hanoi(len(a), a, c, b)
# print(a)
# print(b)
# print(c)
