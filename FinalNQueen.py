import numpy as np
import queue

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False


    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# def heuristic(board):
#     # Number of pairs of queens that are attacking each other
#     conflicts = 0
#     n = len(board)
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1:
#                 # Check rows and columns
#                 for k in range(n):
#                     if k != j and board[i][k] == 1:
#                         conflicts += 1
#                     if k != i and board[k][j] == 1:
#                         conflicts += 1
#                 # Check diagonals
#                 for k in range(n):
#                     for l in range(n):
#                         if k != i and l != j and abs(i - k) == abs(j - l) and board[k][l] == 1:
#                             conflicts += 1
#     return conflicts // 2  # Each pair of queens is counted twice


def count_and_positions(board):
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
 
    for i in range(row - 1, -1, -1): 
        if board[i][col] == 1:
            score += 1
            break

 
    for i in range(row + 1, n): 
        if board[i][col] == 1:
            score += 1
            break

    
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
        if board[i][j] == 1:
            score += 1
            break

  
    for i, j in zip(range(row + 1, n, 1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            score += 1
            break

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            score += 1
            break

    for i, j in zip(range(row + 1, n, 1), range(col + 1, n, 1)):
        if board[i][j] == 1:
            score += 1
            break

    return score

def heuristic(state):
    total = 0
    positions, count = count_and_positions(state) 
    for i in range(count):
        row, col = positions[i]
        total += threat_score(state,row, col)
    return total


def astar_nqueens(n):
    total_steps = 0
    start_state = np.zeros((n, n), dtype=int)
    open_set = queue.PriorityQueue()
    open_set.put((heuristic(start_state), 0, tuple(map(tuple, start_state))))
    closed_states = set()
    while not open_set.empty():
        totalF, cost, current_state = open_set.get()
        current_state = np.array(current_state)

        if tuple(current_state.flatten()) in closed_states:
            continue

        closed_states.add(tuple(current_state.flatten()))

        if np.sum(current_state) == n:
            print("Solution Found:")
            print(current_state)
            print("Total Threat: ", heuristic(current_state))
            print("\nTotal Steps taken: ", total_steps)
            return

        row = np.where(current_state.sum(axis=1) == 0)[0][0]

        for col in range(n):
            if is_safe(current_state, row, col, n):
                new_state = current_state.copy()
                total_steps += 1
                new_state[row, col] = 1
                h = heuristic(new_state)
                g = cost + 1
                f = g + h
                open_set.put((f, g, tuple(map(tuple, new_state))))

        print("Step", cost)
        print(current_state)
        print("Total Threat: ", heuristic(current_state))

    print("No solution found.")

n = int(input("Enter number of Queens: "))
astar_nqueens(n)
