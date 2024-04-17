def solve(frogs):
    frogs = [0] + frogs
    print(frogs)

    idx = 0  # index of the empty position
    counter = 0  # the number of movement
    right = True # flag for movement direction
    finish_cond = [0] + sorted(frogs[1:], reverse=True)

    while frogs != finish_cond:
        # odd
        if len(frogs) % 2 == 0:
            if right:
                if idx + 2 < len(frogs):
                    if frogs[idx + 1] < frogs[idx + 2]:
                        frogs[idx], frogs[idx + 2] = frogs[idx + 2], frogs[idx]
                        print(frogs)
                        idx += 2
                    else:
                        if idx + 3 < len(frogs) and frogs[idx + 2] > frogs[idx + 3]:
                            frogs[idx], frogs[idx + 2] = frogs[idx + 2], frogs[idx]
                            print(frogs)
                            idx += 2
                        else:
                            frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                            print(frogs)
                            idx += 1
                elif idx + 1 < len(frogs):
                    right = False
                    if frogs[idx + 1] == min(frogs) + 1:
                        while frogs[idx - 1] != max(frogs):
                            frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                            counter += 1
                            print(frogs)
                            idx -= 1

                        if idx - 2 == 0:
                            frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                            print(frogs)
                            idx -= 2
                        else:
                            frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                            print(frogs)
                            idx -= 1
                    else:
                        frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                        print(frogs)
                        idx += 1
                else:
                    right = False
                    if frogs[idx - 1] < frogs[idx - 2]:
                        frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                        print(frogs)
                        idx -= 1
                    else:
                        frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                        print(frogs)
                        idx -= 2
            else:
                if idx - 2 >= 0:
                    if frogs[idx - 1] < frogs[idx - 2]:
                        frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                        print(frogs)
                        idx -= 1
                    else:
                        frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                        print(frogs)
                        idx -= 2
                elif idx - 1 >= 0:
                    right = True
                    if frogs[idx + 1] == max(frogs):
                    # if frogs[idx + 1] > frogs[idx - 1]:
                        frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                        print(frogs)
                        idx += 1
                    else:
                        frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                        print(frogs)
                        idx -= 1
                else:
                    right = True
                    if frogs[idx + 1] < frogs[idx + 2]:
                        frogs[idx], frogs[idx + 2] = frogs[idx + 2], frogs[idx]
                        print(frogs)
                        idx += 2
                    else:
                        frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                        print(frogs)
                        idx += 1
        # even
        else:
            # right
            if right:
                if idx + 2 < len(frogs):
                    if frogs[idx + 1] < frogs[idx + 2]:
                        frogs[idx], frogs[idx + 2] = frogs[idx + 2], frogs[idx]
                        print(frogs)
                        idx += 2
                    else:
                        if idx + 3 < len(frogs) and frogs[idx + 2] > frogs[idx + 3] and (frogs[idx + 1] - frogs[idx + 2] < frogs[idx + 2] - frogs[idx + 3]):
                            frogs[idx], frogs[idx + 2] = frogs[idx + 2], frogs[idx]
                            print(frogs)
                            idx += 2
                        else:
                            if finish_cond[idx + 1:] == frogs[idx + 1:]:
                            # if idx - 1 == 0 and frogs[idx - 1] < frogs[idx + 1]:
                                frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                                print(frogs)
                                idx -= 1
                            else:
                                frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                                print(frogs)
                                idx += 1
                # elif idx + 1 < len(frogs):
                #     right = False
                #     if frogs[idx + 1] > frogs[idx - 1]:
                #         frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                #         print(frogs)
                #         idx += 1
                #     else:
                #         frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                #         print(frogs)
                #         idx -= 1
                else:
                    right = False
                    if idx == len(frogs) - 2:
                        if frogs[idx + 1] > frogs[idx - 1]:
                            frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                            print(frogs)
                            idx += 1
                        else:
                            if frogs[idx - 1] > frogs[idx - 2]:
                                frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                                print(frogs)
                                idx -= 2
                            else:
                                frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                                print(frogs)
                                idx -= 1
                    else:
                        if frogs[idx - 1] < frogs[idx - 2]:
                            frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                            print(frogs)
                            idx -= 1
                        else:
                            frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                            print(frogs)
                            idx -= 2
            #left
            else:
                if idx - 2 >= 0:
                    if frogs[idx - 1] < frogs[idx - 2]:
                        if idx + 1 < len(frogs) and frogs[idx + 1] > frogs[idx - 1]:
                            frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                            print(frogs)
                            idx += 1
                        else:
                            frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                            print(frogs)
                            idx -= 1
                    else:
                        if idx - 2 <= 0:
                            right = True
                        frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                        print(frogs)
                        idx -= 2
                else:
                    if frogs[idx + 1] < frogs[idx + 2]:
                        frogs[idx], frogs[idx + 2] = frogs[idx + 2], frogs[idx]
                        print(frogs)
                        idx += 2
                        right = True
                    else:
                        if idx - 1 == 0 and frogs[idx + 1] > frogs[idx - 1]:
                            frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                            print(frogs)
                            idx += 1
                        else:
                            frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                            print(frogs)
                            idx -= 1
                            right = True

        counter += 1
    return counter


state = [int(x) for x in input("Masukkan urutan kodok: ").split(" ")]
# state = [1, 4, 3, 2]
print(solve(state))


# print(solve([2,3,4,5,6,1]))

# import itertools
# test_list = list(reversed([i for i in range(1,5)]))
# test_cases = [list(case) for case in itertools.permutations(test_list, len(test_list))]

# avg = 0
# for i in range(len(test_cases)):
#     print(f"case: {i}")
#     x = solve(test_cases[i])
#     avg += x
#     print(f"count: {x}")
#     print("---------------------------")

# print(f"average: {avg/len(test_cases)}")
