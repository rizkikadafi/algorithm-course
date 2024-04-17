from heapq import heappush, heappop
from enum import IntEnum
import heapq
class Move(IntEnum):
    NONE = 0,
    RIGHT = 1,
    RIGHT2 = 2,
    LEFT = -1,
    LEFT2 = -2

def possibilities_mov(state, prev_mov:Move):
    movements = []
    zero_idx = state.index(0)
    if zero_idx + 2 < len(state):
        if prev_mov != Move.LEFT:
            movements.append(Move.RIGHT)
        if prev_mov != Move.LEFT2:
            movements.append(Move.RIGHT2)
    elif zero_idx + 1 < len(state):
        if prev_mov != Move.LEFT:
            movements.append(Move.RIGHT)

    if zero_idx - 2 >= 0:
        if prev_mov != Move.RIGHT:
            movements.append(Move.LEFT)
        if prev_mov != Move.RIGHT2:
            movements.append(Move.LEFT2)
    elif zero_idx - 1 >= 0:
        if prev_mov != Move.RIGHT:
            movements.append(Move.LEFT)

    return movements


def get_priority_elm(state, goals):
    result = {}
    for idx, elm in enumerate(state):
        if elm == 0: continue
        result[elm] = abs(goals.index(elm) - idx)
    return result

def get_focus_elm(state, priority_elm, possibilities_mov):
    zero_idx = state.index(0)
    result = []
    for move in possibilities_mov:
        match move:
            case Move.RIGHT:
                heappush(result, (-priority_elm[state[zero_idx + 1]], state[zero_idx + 1]))
            case Move.RIGHT2:
                heappush(result, (-priority_elm[state[zero_idx + 2]], state[zero_idx + 2]))
            case Move.LEFT:
                heappush(result, (-priority_elm[state[zero_idx - 1]], state[zero_idx - 1]))
            case Move.LEFT2:
                heappush(result, (-priority_elm[state[zero_idx - 2]], state[zero_idx - 2]))

    res = heapq.nsmallest(2, result)
    if len(res) > 1 and res[0][0] == res[1][0]:
        return res[1][1]
    else:
        return heappop(result)[1]

def get_mov(state, goals, possibilities_mov, focus_elm):
    if len(possibilities_mov) == 1:
        return possibilities_mov[0]

    zero_idx = state.index(0)
    goals_focus_elm_idx = goals.index(focus_elm)
    focus_elm_idx = state.index(focus_elm)
    result = []
    
    for move in possibilities_mov:
        match move:
            case Move.RIGHT:
                if state[zero_idx + 1] == focus_elm:
                    heappush(result, (abs(zero_idx - goals_focus_elm_idx), Move.RIGHT))
                else:
                    if zero_idx + 1 == focus_elm_idx + 1 or zero_idx + 1 == focus_elm_idx + 2 or zero_idx + 1 == focus_elm_idx - 1 or zero_idx + 1 == focus_elm_idx - 2:
                        heappush(result, (abs(zero_idx + 1 - goals_focus_elm_idx), Move.RIGHT))
                    else:
                        heappush(result, (abs(focus_elm_idx - goals_focus_elm_idx), Move.RIGHT))
            case Move.RIGHT2:
                if state[zero_idx + 2] == focus_elm:
                    heappush(result, (abs(zero_idx - goals_focus_elm_idx), Move.RIGHT2))
                else:
                    if zero_idx + 2 == focus_elm_idx + 1 or zero_idx + 2 == focus_elm_idx + 2 or zero_idx + 2 == focus_elm_idx - 1 or zero_idx + 2 == focus_elm_idx - 2:
                        heappush(result, (abs(zero_idx + 2 - goals_focus_elm_idx), Move.RIGHT2))
                    else:
                        heappush(result, (abs(focus_elm_idx - goals_focus_elm_idx), Move.RIGHT2))
            case Move.LEFT:
                if state[zero_idx - 1] == focus_elm:
                    heappush(result, (abs(zero_idx - goals_focus_elm_idx), Move.LEFT))
                else:
                    if zero_idx - 1 == focus_elm_idx + 1 or zero_idx - 1 == focus_elm_idx + 2 or zero_idx - 1 == focus_elm_idx - 1 or zero_idx - 1 == focus_elm_idx - 2:
                        heappush(result, (abs(zero_idx - 1 - goals_focus_elm_idx), Move.LEFT))
                    else:
                        heappush(result, (abs(focus_elm_idx - goals_focus_elm_idx), Move.LEFT))
            case Move.LEFT2:
                if state[zero_idx - 2] == focus_elm:
                    heappush(result, (abs(zero_idx - goals_focus_elm_idx), Move.LEFT2))
                else:
                    if zero_idx - 2 == focus_elm_idx + 1 or zero_idx - 2 == focus_elm_idx + 2 or zero_idx - 2 == focus_elm_idx - 1 or zero_idx - 2 == focus_elm_idx - 2:
                        heappush(result, (abs(zero_idx - 2 - goals_focus_elm_idx), Move.LEFT2))
                    else:
                        heappush(result, (abs(focus_elm_idx - goals_focus_elm_idx), Move.LEFT2))

    res = heapq.nsmallest(2, result)
    if len(res) > 1 and res[0][0] == res[1][0]:
        return res[1][1]
    else:
        return heappop(result)[1]

def solve(frogs):
    frogs = [0] + frogs
    print(frogs)

    idx = 0  # index of the empty position
    counter = 0  # the number of movement
    finish_cond = [0] + sorted(frogs[1:], reverse=True)

    prev_mov = Move.NONE
    while frogs != finish_cond:
        possibilities = possibilities_mov(frogs, prev_mov)
        priority_elms = get_priority_elm(frogs, finish_cond)
        focus_elm = get_focus_elm(frogs, priority_elms, possibilities)
        move = get_mov(frogs, finish_cond, possibilities, focus_elm)
        prev_mov = move
        match move:
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


frogs = [int(x) for x in input("Masukkan urutan kodok: ").split(" ")]
# frogs = [6, 5, 4, 2, 3, 1]
print(solve(frogs))

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
