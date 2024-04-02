from heapq import heappush, heappop

def count_misplaced(current_state, goal_state):
    return sum(1 for a, b in zip(current_state, goal_state) if a != b)

def generate_moves(state):
    moves = []
    zero_index = state.index(0)
    if zero_index + 2 < len(state):
        moves.append(state[:zero_index] + [state[zero_index+1], 0] + state[zero_index+2:])
        moves.append(state[:zero_index]+ [state[zero_index + 2]] + [state[zero_index + 1], 0] + (state[zero_index+3:] if zero_index + 3 < len(state) else []))
    elif zero_index + 1 < len(state):
        moves.append(state[:zero_index] + [state[zero_index+1], 0] + state[zero_index+2:])

    if zero_index - 2 >= 0:
        moves.append(state[:zero_index-1] + [0, state[zero_index-1]] + (state[zero_index+1:] if zero_index + 1 < len(state) else []))
        moves.append(state[:zero_index-2] + [0, state[zero_index - 1]] + [state[zero_index - 2]] + (state[zero_index+1:] if zero_index + 1 < len(state) else []))
    elif zero_index - 1 >= 0:
        moves.append(state[:zero_index-1] + [0, state[zero_index-1]] + (state[zero_index+1:] if zero_index + 1 < len(state) else []))

    return moves

def a_star_count_moves(start_state: list, goal_state: list):
    frontier = [(0, start_state, 0, [])]  # Prioritas, keadaan, jumlah langkah, jalur gerakan
    explored = set()
    while frontier:
        _, current_state, moves, path = heappop(frontier)  # Ambil keadaan dengan prioritas terendah
        if current_state == goal_state:
            return current_state, moves, path
        explored.add(tuple(current_state))
        for move in generate_moves(current_state):
            if tuple(move) not in explored:
                priority = count_misplaced(move, goal_state) + moves + 1
                heappush(frontier, (priority, move, moves + 1, path + [move]))

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
start_state = [0] + state
goal_state = [0] + sorted(state, reverse=True)
result, moves, path = a_star_count_moves(start_state, goal_state)
print(start_state)
for move in path:
    print(move)
print("Jumlah gerakan minimal:", moves)
print("--------------------------------")

