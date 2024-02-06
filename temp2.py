import numpy as np

class StateGenerator:
    def __init__(self, n):
        self.n = n
        self.current_state = None
        self.states = {}  # Make states an instance attribute

    def generate_states(self, state):
        # state = np.copy(state)
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] == 1:
                    state[i][j] = 0
                    state[i][(j + 1) % self.n] = 1  # Correct modulo calculation
                    ones_coords = [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 1]
                # Use coordinates as key
                    key = tuple(ones_coords)
                    if key not in self.states:
                        self.states[key] = total_threat(state)

    def reconstruct_state(self, ones_coords):
        state = np.zeros((self.n, self.n))
        for coord in ones_coords.keys():
            state[coord[0]][coord[1]] = 1
        return state
    
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


n = int(input("Enter number of Queens: "))
board = np.zeros((n, n), dtype=int)
for i in range(n):
    board[i][0] = 1

print("Initial State")
print(board)
print()

all = StateGenerator(4)
all.generate_states(board)

for element in all.states:
    state = all.reconstruct_state(all.states)
    print(state)