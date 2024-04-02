def solve(frogs):
    # focusing on empty position movement instead of frog movement
    idx = 0 # index of the empty position
    counter = 0 # the number of movement
    right = True # flag for movement direction
    if len(frogs) % 2 != 0:
        # movement for odd case
        while True:
            if right:
                if idx + 2 > len(frogs) - 1:
                    frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                    counter += 1
                    print(frogs)
                    idx -= 1
                    right = False
                else:
                    frogs[idx], frogs[idx + 2] = frogs[idx + 2], frogs[idx]
                    counter += 1
                    print(frogs)
                    idx += 2
            else:
                if idx - 2 < 0:
                    frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                    print(frogs)
                    counter += 1
                    idx -= 1
                    right = True
                else:
                    frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                    counter += 1
                    print(frogs)
                    idx -= 2

            if frogs[0] == 0 and sorted(frogs[1:], reverse=True) == frogs[1:]:
                return counter
    else:
        # movement for even case
        while True:
            if right:
                if idx + 2 > len(frogs) - 1:
                    if frogs[idx + 1] == min(frogs) + 1:
                        while frogs[idx - 1] != max(frogs):
                            frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                            counter += 1
                            print(frogs)
                            idx -= 1

                        frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                        counter += 1
                        print(frogs)
                        idx -= 2
                    else:
                        frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                        counter += 1
                        print(frogs)
                        idx += 1
                    right = False
                else:
                    frogs[idx], frogs[idx + 2] = frogs[idx + 2], frogs[idx]
                    counter += 1
                    print(frogs)
                    idx += 2
            else:
                if idx - 2 < 0:
                    if frogs[idx + 1] == max(frogs):
                        frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                        counter += 1
                        print(frogs)
                        idx += 1
                    else:
                        frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                        counter += 1
                        print(frogs)
                        idx -= 1
                    right = True
                else:
                    frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                    counter += 1
                    print(frogs)
                    idx -= 2

            if frogs[0] == 0 and sorted(frogs[1:], reverse=True) == frogs[1:]:
                return counter

frogs = [int(x) for x in input("Masukkan urutan kodok: ").split()]
frogs = [0] + frogs
print(frogs)
print("minimal movement:", solve(frogs))
