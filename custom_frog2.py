from enum import IntEnum
class Move(IntEnum):
    NONE = 0,
    RIGHT = 1,
    RIGHT2 = 2,
    LEFT = -1,
    LEFT2 = -2

def possibilities_mov(state, goals, prev_mov:Move):
    movements = []
    right_place = []
    zero_idx = state.index(0)
    if zero_idx + 2 < len(state):
        if prev_mov != Move.LEFT:
            movements.append(Move.RIGHT)
            right_place.append((goals.index(state[zero_idx + 1]) == zero_idx + 1))
        if prev_mov != Move.LEFT2:
            movements.append(Move.RIGHT2)
            right_place.append((goals.index(state[zero_idx + 2]) == zero_idx + 2))
    elif zero_idx + 1 < len(state):
        if prev_mov != Move.LEFT:
            movements.append(Move.RIGHT)
            right_place.append((goals.index(state[zero_idx + 1]) == zero_idx + 1))

    if zero_idx - 2 >= 0:
        if prev_mov != Move.RIGHT:
            movements.append(Move.LEFT)
            right_place.append((goals.index(state[zero_idx - 1]) == zero_idx - 1))
        if prev_mov != Move.RIGHT2:
            movements.append(Move.LEFT2)
            right_place.append((goals.index(state[zero_idx - 2]) == zero_idx - 2))
    elif zero_idx - 1 >= 0:
        if prev_mov != Move.RIGHT:
            movements.append(Move.LEFT)
            right_place.append((goals.index(state[zero_idx - 1]) == zero_idx - 1))

    if all(right_place):
        return [movements.pop()]

    return movements



def get_mov(state, goals, possibilities_mov):
    zero_idx = state.index(0)
    acc = []
    for move in possibilities_mov:
        match move:
            case Move.RIGHT:
                priority = abs(goals.index(state[zero_idx + Move.RIGHT.value])-zero_idx)
                right_place = (goals.index(state[zero_idx + Move.RIGHT.value]) == zero_idx + Move.RIGHT.value)
                acc.append((priority, Move.RIGHT, right_place))
            case Move.RIGHT2:
                priority = abs(goals.index(state[zero_idx + Move.RIGHT2.value])-zero_idx)
                right_place = (goals.index(state[zero_idx + Move.RIGHT2.value]) == zero_idx + Move.RIGHT2.value)
                acc.append((priority, Move.RIGHT2, right_place))
            case Move.LEFT:
                priority = abs(goals.index(state[zero_idx + Move.LEFT.value])-zero_idx)
                right_place = (goals.index(state[zero_idx + Move.LEFT.value]) == zero_idx + Move.LEFT.value)
                acc.append((priority, Move.LEFT, right_place))
            case Move.LEFT2:
                priority = abs(goals.index(state[zero_idx + Move.LEFT2.value])-zero_idx)
                right_place = (goals.index(state[zero_idx + Move.LEFT2.value]) == zero_idx + Move.LEFT2.value)
                acc.append((priority, Move.LEFT2, right_place))

    if all([rl[2] for rl in acc]):
        return max(acc)

    return min(acc)

# print(get_mov([4, 0, 3, 2, 1], [0,4,3,2,1], possibilities_mov([4, 0, 3, 2, 1], Move.LEFT2)))


def solve(frogs):
    frogs = [0] + frogs
    print(frogs)

    idx = 0  # index of the empty position
    counter = 0  # the number of movement
    # right = True # flag for movement direction
    finish_cond = [0] + sorted(frogs[1:], reverse=True)

    prev_mov = Move.NONE
    while frogs != finish_cond:
        move = get_mov(frogs, finish_cond, possibilities_mov(frogs, finish_cond, prev_mov))
        prev_mov = move[1]
        match move[1]:
            case Move.RIGHT:
                frogs[idx], frogs[idx + 1] = frogs[idx + 1], frogs[idx]
                idx += 1
            case Move.RIGHT2:
                frogs[idx], frogs[idx + 2] = frogs[idx + 2], frogs[idx]
                idx += 2
            case Move.LEFT:
                frogs[idx], frogs[idx - 1] = frogs[idx - 1], frogs[idx]
                idx -= 1
            case Move.LEFT2:
                frogs[idx], frogs[idx - 2] = frogs[idx - 2], frogs[idx]
                idx -= 2
        print(frogs)
        counter += 1
    return counter



# print(solve([5, 4, 3, 1, 2]))
import itertools
test_list = list(reversed([i for i in range(1,4)]))
test_cases = [list(case) for case in itertools.permutations(test_list, len(test_list))]

# print(solve(test_cases[6]))


# n = int(input())
# print(solve(test_cases[n]))

avg = 0
for i in range(len(test_cases)):
    print(f"case: {i}")
    x = solve(test_cases[i])
    avg += x
    print(f"count: {x}")
    print("---------------------------")

print(f"average: {avg/len(test_cases)}")
