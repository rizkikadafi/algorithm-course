from collections import deque

def heuristic(board):
    # Heuristic function: count the number of frogs that are not in their target positions
    misplaced = sum(1 for i, frog in enumerate(board) if frog is not None and i != len(board) - frog)
    return misplaced

# Greed Best-First Search algorithm used for traversing the highest priority board from all the possible states
def gbfs_algo(board, target, step=False):
    queue = deque([(board, 0)])  
    visited = set()  

    while queue:
        current_board, moves = queue.popleft()

        # Print current state of the board
        if step == True:
            print("[{}]".format(", ".join(str(elem) for elem in current_board)))

        # Base case to check if target state is reached
        if current_board == target:
            return moves

        # Generate possible next states
        next_states = []
        i = current_board.index(None)

        # Try moving the frog to the right
        if i - 1 >= 0:
            new_board = current_board[:]
            new_board[i-1], new_board[i] = new_board[i], new_board[i-1]
            next_states.append((new_board, moves + 1))

        # Try jumping the frog to the right 
        if i - 2 >= 0:
            new_board = current_board[:]
            new_board[i-2], new_board[i] = new_board[i], new_board[i-2]
            next_states.append((new_board, moves + 1))

        # Try moving the frog to the left
        if i + 1 < len(current_board):
            new_board = current_board[:]
            new_board[i+1], new_board[i] = new_board[i], new_board[i+1]
            next_states.append((new_board, moves + 1))

        # Try jumping the frog to the left
        if i + 2 < len(current_board):
            new_board = current_board[:]
            new_board[i+2], new_board[i] = new_board[i], new_board[i+2]
            next_states.append((new_board, moves + 1))

        # Sort next states based on heuristic value
        next_states.sort(key=lambda x: heuristic(x[0]))

        # Add sorted next states to the queue
        for state in next_states:
            if tuple(state[0]) not in visited:
                queue.append(state)
                visited.add(tuple(state[0]))

    return -1


# User input
def main() -> None:
    # Initiatlized initial state
    initial_state = [None]
    num_of_frogs = int(input("Insert the number of frogs: "))
    for x in range(1, num_of_frogs + 1):
        frog = int(input(f"Please input the frog for position {x}: "))
        initial_state.append(frog)

    step = True if input("Do you want to print every state of the board traversed? (Y/n) ").lower() == "y" else False

    # Initiatlized target state
    target_state = [None] + list(range(num_of_frogs, 0, -1))

    # Find minimum moves using Greedy Best-First Search
    min_moves = gbfs_algo(initial_state, target_state, step)

    # Print the answer
    print("\nThe fewest moves possible is", min_moves)


if __name__ == '__main__':
    main()


