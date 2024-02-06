import numpy as np
import queue

n = int(input("Enter number of Queens: "))
board = np.zeros((n, n), dtype=int)


def count_queens_and_positions(board):
    count = 0
    positions = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                count += 1
                positions.append((i, j))
    return positions, count


def threat_score(board, row, col):
    score = 0
    n = len(board)
    # checking col above
    for i in range(row - 1, -1, -1): #we start with row - 1 so we dont count the current queen
        if board[i][col] == 1:
            score += 1
            break

    # checking col below
    for i in range(row + 1, n): # here we're moving up so we do row + 1
        if board[i][col] == 1:
            score += 1
            break

    # checking positive diagonal moving up
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
        if board[i][j] == 1:
            score += 1
            break

    # checking positive diagonal moving down
    for i, j in zip(range(row + 1, n, 1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            score += 1
            break

    # checking negative diagonal moving up
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            score += 1
            break

    # checking negative diagonal moving down
    for i, j in zip(range(row + 1, n, 1), range(col + 1, n, 1)):
        if board[i][j] == 1:
            score += 1
            break

    return score


def total_threat(board):
    total = 0
    positions, count = count_queens_and_positions(board)  # board argument was missing
    for i in range(count):
        row, col = positions[i]
        total += threat_score(board,row, col)
    return total


def print_values(g, h, f):
    print("g(x): ", g)
    print("h(x): ", h)
    print("f(x): ", f)

def generate_start_state(n):
    start_state = np.zeros((n, n), dtype=int)
    for i in range(n):
        start_state[i][0] = 1
    return start_state  # Add this line

def generate_states(board):
    states = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 0 and is_valid_move(board, row, col):  # Check if it's a valid move
                new_state = board.copy()
                new_state[row, col] = 1
                states.append(new_state)
    print(f"Generated {len(states)} states")  # Add this line
    return states

def a_star_n_queens():
    start_state = generate_start_state(n)
    print("Start state: \n", start_state)
    print_values(1, total_threat(start_state), total_threat(start_state) + 1)
    open_list = queue.PriorityQueue()
    open_list.put((total_threat(start_state), start_state))
    closed_set = set()

    while not open_list.empty():
        current_state = open_list.get()[1]
        closed_set.add(tuple(map(tuple, current_state)))

        if total_threat(current_state) == 0:
            return current_state

        states = generate_states(current_state)  # current_state argument was missing
        for state in states:
            if tuple(map(tuple, state)) not in closed_set:
                open_list.put((total_threat(state), state))
                print("New state:", state)

    return None


def is_valid_move(board, row, col):
    n = len(board)

    # Check the same row
    for i in range(n):
        if board[row][i] == 1:
            return False

    # Check the same column
    for i in range(n):
        if board[i][col] == 1:
            return False

    # Check the main diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the secondary diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True





solution = a_star_n_queens()  # Solve for n-queens



