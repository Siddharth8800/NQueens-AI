import numpy as np
import queue
import itertools

n = int(input("Enter number of Queens: "))
state = np.zeros((n, n), dtype=int)
history = {}
for i in range(n):
    state[i][0] = 1


def generate_goal():
    state = np.zeros((n, n), dtype=int)
    successors = []

    def is_diagonal_occupied(x, y, temp_state):
        for i in range(n):
            for j in range(n):
                if temp_state[i][j] == 1 and (i-j == x-y or i+j == x+y):
                    return True
        return False

    if np.all(state == 0):
        for perm in itertools.permutations(range(n)):
            successor = np.zeros((n, n), dtype=int)
            for i, j in enumerate(perm):
                if 1 not in successor[:, j] and not is_diagonal_occupied(i, j, successor):
                    successor[i][j] = 1
                else:
                    break
            else:
                successors.append(successor)
    else: 
        for i in range(n):
            for j in range(n):
                if state[i][j] == 1:
                    for k in range(1, n):
                        new_j = (j+k)%n
                        if 1 not in state[:, new_j] and not is_diagonal_occupied(i, new_j, state): 
                            successor = np.copy(state)
                            successor[i][j] = 0
                            successor[i][new_j] = 1
                            successors.append(successor)
                            break  
    return successors 



def generate_successors(state, previous_states):
    """Generate all possible successors of a state."""
    n = len(state)
    successors = []

    def state_to_str(state):
        """Convert a state to a string."""
        return '\n'.join(''.join(str(cell) for cell in row) for row in state)

    if np.all(state == 0):  # Check if the state is a zero matrix
        for i in range(n):  # Generate n successors
            successor = np.zeros((n, n), dtype=int)
            j = np.random.choice(n)  # Choose a random column
            successor[i][j] = 1
            successor_str = state_to_str(successor)
            if successor_str not in previous_states:  # Check if the successor is a new state
                successors.append(successor)
                previous_states[successor_str] = 1  # Add the new state to the history
    else:
        for i in range(n):  # Generate n successors
            successor = np.copy(state)
            if 1 in successor[i]:
                j = np.random.choice(n)  # Choose a random column
                successor[i] = 0  # Clear the current row
                successor[i][j] = 1  # Place the 1 in the new column
                successor_str = state_to_str(successor)
                if successor_str not in previous_states:  # Check if the successor is a new state
                    successors.append(successor)
                    previous_states[successor_str] = 1  # Add the new state to the history

    return successors



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

def heuristic(state):
    total = 0
    positions, count = count_and_positions(state)  # board argument was missing
    for i in range(count):
        row, col = positions[i]
        total += threat_score(state,row, col)
    return total

goal = generate_goal()

def a_star(start, goal):
    open_list = queue.PriorityQueue()
    open_list.put((cost(start) + heuristic(start), start))
    closed_list = set()
    g = {str(start): 0}
    parents = {str(start): None}

    while not open_list.empty():
        _, current = open_list.get()
        if np.array_equal(current, goal):
            path = []
            while current is not None:
                path.append(current)
                current = parents[str(current)]
            path.reverse()
            return path
        closed_list.add(str(current))
        for successor in generate_successors(current):
            successor_str = str(successor)
            successor_g = g[str(current)] + cost(successor)
            if successor_str in closed_list:
                continue
            if successor_g < g.get(successor_str, float('inf')):
                open_list.put((successor_g + heuristic(successor), successor))
                g[successor_str] = successor_g
                parents[successor_str] = current
    return None

path = a_star(state, goal)
print("The path to the goal state is:", path)