import numpy as np
import itertools

n = int(input("Enter number of Queens: "))


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