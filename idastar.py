from heapq import heappush, heappop
import concurrent.futures

from enum import Enum
class Move(Enum):
    NONE = 0,
    RIGHT = 1,
    RIGHT2 = 2,
    LEFT = -1,
    LEFT2 = -2

def count_misplaced(current_state, goal_state):
    return sum(1 for a, b in zip(current_state, goal_state) if a != b)

def generate_moves(state, prev_move):
    moves = []
    current_move = []
    zero_index = state.index(0)
    if zero_index + 2 < len(state):
        if prev_move != (0, 1, 0):
            current_move = state[:zero_index] + [state[zero_index+1], 0] + state[zero_index+2:]
            moves.append((current_move, (1, 1, 0)))

        if prev_move != (0, 0, 1):
            current_move =state[:zero_index]+ [state[zero_index + 2]] + [state[zero_index + 1], 0] + (state[zero_index+3:] if zero_index + 3 < len(state) else []) 
            moves.append((current_move, (1, 0, 1)))

    elif zero_index + 1 < len(state):
        current_move = state[:zero_index] + [state[zero_index+1], 0] + state[zero_index+2:]
        moves.append((current_move, (1, 1, 0)))

    if zero_index - 2 >= 0:
        if prev_move != (1, 1, 0):
            current_move = state[:zero_index-1] + [0, state[zero_index-1]] + (state[zero_index+1:] if zero_index + 1 < len(state) else []) 
            moves.append((current_move, (0, 1, 0)))

        if prev_move != (1, 0, 1):
            current_move = state[:zero_index-2] + [0, state[zero_index - 1]] + [state[zero_index - 2]] + (state[zero_index+1:] if zero_index + 1 < len(state) else []) 
            moves.append((current_move, (0, 0, 1)))

    elif zero_index - 1 >= 0:
        if prev_move != (1, 1, 0):
            current_move = state[:zero_index-1] + [0, state[zero_index-1]] + (state[zero_index+1:] if zero_index + 1 < len(state) else []) 
            moves.append((current_move, (0, 1, 0)))

    return moves

def a_star_count_moves(start_state: list, goal_state: list):
    frontier = [(0, start_state, 0, [], (-1, 0, 0))]  # Prioritas, keadaan, jumlah langkah, jalur gerakan
    explored = set()
    while frontier:
        _, current_state, moves, path, prev_move = heappop(frontier)  # Ambil keadaan dengan prioritas terendah
        if current_state == goal_state:
            return current_state, moves, path
        explored.add(tuple(current_state))
        for move, current_move in generate_moves(current_state, prev_move):
            if tuple(move) not in explored:
                priority = count_misplaced(move, goal_state) + moves + 1
                heappush(frontier, (priority, move, moves + 1, path + [move], current_move))


def solve_with_concurrency(start_state, goal_state, max_workers=4):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future = executor.submit(a_star_count_moves, start_state, goal_state)
        result, moves, path = future.result()
        return result, moves, path

# import itertools
# test_list = list(reversed([i for i in range(1,11)]))
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


start_state = [0,1,2,3,4,5,6,7,8] 
goal_state = [0,8,7,6,5,4,3,2,1]

import time
start = time.time()

# result, moves, path = a_star_count_moves(start_state, goal_state)
result, moves,path = solve_with_concurrency(start_state, goal_state)

end = time.time()

print(f"time: {end - start}")
print(start_state)
for move in path:
    print(move)
print("Jumlah gerakan minimal:", moves)
print("--------------------------------")

