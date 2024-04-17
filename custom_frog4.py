from heapq import heappush, heappop

from enum import IntEnum
class Move(IntEnum):
    NONE = 0,
    RIGHT = 1,
    RIGHT2 = 2,
    LEFT = -1,
    LEFT2 = -2

def get_next_move(state, move):
    zero_index = state.index(0)
    match move:
        case move.RIGHT:
            return state[:zero_index] + [state[zero_index+1], 0] + state[zero_index+2:]
        case move.RIGHT2:
            return state[:zero_index]+ [state[zero_index + 2]] + [state[zero_index + 1], 0] + (state[zero_index+3:] if zero_index + 3 < len(state) else [])
        case move.LEFT:
            return state[:zero_index-1] + [0, state[zero_index-1]] + (state[zero_index+1:] if zero_index + 1 < len(state) else [])
        case move.LEFT2:
            return state[:zero_index-2] + [0, state[zero_index - 1]] + [state[zero_index - 2]] + (state[zero_index+1:] if zero_index + 1 < len(state) else [])


def generate_path(start_state, move):
    zero_index = start_state.index(0)
    match move:
        case Move.RIGHT:
            start_state[zero_index], start_state[zero_index+1] = start_state[zero_index+1], start_state[zero_index]
        case Move.RIGHT2:
            start_state[zero_index], start_state[zero_index+2] = start_state[zero_index+2], start_state[zero_index]
        case Move.LEFT:
            start_state[zero_index], start_state[zero_index-1] = start_state[zero_index-1], start_state[zero_index]
        case Move.LEFT2:
            start_state[zero_index], start_state[zero_index-2] = start_state[zero_index-2], start_state[zero_index]


def count_misplaced(current_state, goal_state):
    return sum(1 for a, b in zip(current_state, goal_state) if a != b)

def generate_moves(state, prev_move):
    moves = []
    zero_index = state.index(0)
    if zero_index + 2 < len(state):
        if prev_move != Move.LEFT:
            moves.append(Move.RIGHT) # RIGHT
        if prev_move != Move.LEFT2:
            moves.append(Move.RIGHT2) # RIGHT2
    elif zero_index + 1 < len(state):
        if prev_move != Move.LEFT:
            moves.append(Move.RIGHT) # RIGHT

    if zero_index - 2 >= 0:
        if prev_move != Move.RIGHT:
            moves.append(Move.LEFT) # LEFT
        if prev_move != Move.RIGHT2:
            moves.append(Move.LEFT2) # LEFT2
    elif zero_index - 1 >= 0:
        if prev_move != Move.RIGHT:
            moves.append(Move.LEFT) # LEFT

    return moves

def a_star_count_moves(start_state: list, goal_state: list):
    frontier = [(0, start_state, 0, [], Move.NONE)]  # Priority, state, step, path
    explored = set()
    while frontier:
        _, current_state, moves, path, prev_move = heappop(frontier)  # Ambil keadaan dengan prioritas terendah
        if current_state == goal_state:
            return current_state, moves, path
        explored.add(tuple(current_state))
        for move in generate_moves(current_state, prev_move):
            next_move = get_next_move(current_state, move)
            if tuple(next_move) not in explored:
                priority = count_misplaced(next_move, goal_state) + moves + 1
                # frontier = []
                heappush(frontier, (priority, next_move, moves + 1, path + [move], move))

# import itertools
# test_list = list(reversed([i for i in range(1,4)]))
# test_cases = [list(case) for case in itertools.permutations(test_list, len(test_list))]

# for i in range(len(test_cases)):
#     start_state = [0] + test_cases[i]
#     goal_state = [0] + test_cases[0]
#     result, moves, path = a_star_count_moves(start_state, goal_state)
#     print(start_state)
#     for move in path:
#         print(move)
#     print("Jumlah gerakan minimal:", moves)
#     print("--------------------------------")


state = [int(x) for x in input("Masukkan urutan kodok: ").split()]
# state = [1,2,3]
start_state = [0] + state
goal_state = [0] + sorted(state, reverse=True)
result, moves, path = a_star_count_moves(start_state, goal_state)

print(start_state)
for move in path:
    # print(move)
    generate_path(start_state, move)
    print(start_state)
print("Jumlah gerakan minimal:", moves)
print("--------------------------------")

# import itertools
# test_list = list(reversed([i for i in range(1,5)]))
# test_cases = [list(case) for case in itertools.permutations(test_list, len(test_list))]

# avg = 0
# for i in range(len(test_cases)):
#     print(f"case: {i}")
#     start_state = [0] + test_cases[i]
#     goal_state = [0] + test_cases[0]
#     result, moves, path = a_star_count_moves(start_state, goal_state)
#     print(start_state)
#     for move in path:
#         print(move)
#     print("Jumlah gerakan minimal:", moves)
#     print("--------------------------------")
#     avg += moves

# print(f"average: {avg/len(test_cases)}")

