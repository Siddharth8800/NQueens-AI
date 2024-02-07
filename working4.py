import numpy as np
import queue
import itertools

n = int(input("Enter number of Queens: "))
state = np.zeros((n, n), dtype=int)
# for i in range(n):
#     state[i][0] = 1

def create_state(n):
    state = np.zeros((n, n), dtype=int)
    cols = np.random.permutation(n)
    for i in range(n):
        state[i, cols[i]] = 1
    return state


# def create_state(n):
#     """Create an nxn matrix with one 1 in each row."""
#     state = np.zeros((n, n), dtype=int)
#     for i in range(n):
#         state[i, np.random.randint(n)] = 1
#     return state

# def state_exists(state, closed_list):
#     """Check if a state exists in the closed list."""
#     state_str = str(state.tolist())
#     return state_str in closed_list

# state = create_state(n)
# string_state = str(state)
# print(state)
# print()
# print("The converted string: \n", string_state)
# print(type(string_state))


# def generate_successors(state):
#     """Generate all possible successors of a state."""
#     n = len(state)
#     successors = []

#     if np.all(state == 0):  # Check if the state is a zero matrix
#         for perm in itertools.permutations(range(n)):
#             successor = np.zeros((n, n), dtype=int)
#             for i, j in enumerate(perm):
#                 successor[i][j] = 1
#             successors.append(successor)
#     else:
#         for i in range(n):
#             for j in range(n):
#                 if state[i][j] == 1:
#                     # Move the 1 to the next column
#                     for k in range(1, n):
#                         new_j = (j+k)%n
#                         if 1 not in state[:, new_j]:  # Check if the column is free
#                             successor = np.copy(state)
#                             successor[i][j] = 0
#                             successor[i][new_j] = 1
#                             successors.append(successor)
#     return successors


# def generate_successors(state):
#     """Generate all possible successors of a state."""
#     n = len(state)
#     successors = []

#     # Generate all permutations of the numbers from 0 to n-1
#     for perm in itertools.permutations(range(n)):
#         successor = np.zeros((n, n), dtype=int)
#         for i, j in enumerate(perm):
#             successor[i][j] = 1
#         successors.append(successor)

#     return successors



# def generate_successors(state):
#     """Generate all possible successors of a state."""
#     n = len(state)
#     successors = []

#     def is_diagonal_occupied(x, y):
#         """Check if the diagonal at position (x, y) is occupied by a 1."""
#         for i in range(n):
#             for j in range(n):
#                 if state[i][j] == 1 and (i-j == x-y or i+j == x+y):
#                     return True
#         return False

#     for i in range(n):
#         for j in range(n):
#             if state[i][j] == 1:
#                 # Move the 1 to the next free column in the same row
#                 for k in range(1, n):
#                     new_j = (j+k)%n
#                     if 1 not in state[:, new_j] and not is_diagonal_occupied(i, new_j):  # Check if the column and diagonal are free
#                         successor = np.copy(state)
#                         successor[i][j] = 0
#                         successor[i][new_j] = 1
#                         successors.append(successor)
#                         break  # Move to the next row after finding a free column
#     return successors[:4]  # Return only the first four successors





def generate_successors(state):
    """Generate all possible successors of a state."""
    n = len(state)
    successors = []

    def is_diagonal_occupied(x, y, temp_state):
        """Check if the diagonal at position (x, y) is occupied by a 1."""
        for i in range(n):
            for j in range(n):
                if temp_state[i][j] == 1 and (i-j == x-y or i+j == x+y):
                    return True
        return False

    if np.all(state == 0):  # Check if the state is a zero matrix
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
                    # Move the 1 to the next free column in the same row
                    for k in range(1, n):
                        new_j = (j+k)%n
                        if 1 not in state[:, new_j] and not is_diagonal_occupied(i, new_j, state):  # Check if the column and diagonal are free
                            successor = np.copy(state)
                            successor[i][j] = 0
                            successor[i][new_j] = 1
                            successors.append(successor)
                            break  # Move to the next row after finding a free column
    return successors[:1]  # Return only the first four successors




# def generate_successors(state):
#     """Generate all possible successors of a state."""
#     n = len(state)
#     successors = []

#     if np.all(state == 0):  # Check if the state is a zero matrix
#         for i in range(n):  # Generate n successors
#             successor = np.zeros((n, n), dtype=int)
#             j = np.random.choice(n)  # Choose a random column
#             successor[i][j] = 1
#             successors.append(successor)
#     else:
#         for i in range(n):  # Generate n successors
#             successor = np.copy(state)
#             if 1 in successor[i]:
#                 j = np.random.choice(n)  # Choose a random column
#                 successor[i] = 0  # Clear the current row
#                 successor[i][j] = 1  # Place the 1 in the new column
#             successors.append(successor)

#     return successors


# def generate_successors(state):
#     """Generate all possible successors of a state."""
#     n = len(state)
#     successors = []

#     for i in range(n):
#         for j in range(n):
#             if state[i][j] == 1:
#                 # Move the 1 to the next free column in the same row
#                 for k in range(1, n):
#                     new_j = (j+k)%n
#                     if 1 not in state[:, new_j]:  # Check if the column is free
#                         successor = np.copy(state)
#                         successor[i][j] = 0
#                         successor[i][new_j] = 1
#                         successors.append(successor)
#                         break  # Move to the next row after finding a free column
#     return successors  # Return only the first four successors


# def generate_successors(state, previous_states):
#     """Generate all possible successors of a state."""
#     n = len(state)
#     successors = []

#     def state_to_str(state):
#         """Convert a state to a string."""
#         return '\n'.join(''.join(str(cell) for cell in row) for row in state)

#     if np.all(state == 0):  # Check if the state is a zero matrix
#         for i in range(n):  # Generate n successors
#             successor = np.zeros((n, n), dtype=int)
#             j = np.random.choice(n)  # Choose a random column
#             successor[i][j] = 1
#             successor_str = state_to_str(successor)
#             if successor_str not in previous_states:  # Check if the successor is a new state
#                 successors.append(successor)
#                 previous_states[successor_str] = 1  # Add the new state to the history
#     else:
#         for i in range(n):  # Generate n successors
#             successor = np.copy(state)
#             if 1 in successor[i]:
#                 j = np.random.choice(n)  # Choose a random column
#                 successor[i] = 0  # Clear the current row
#                 successor[i][j] = 1  # Place the 1 in the new column
#                 successor_str = state_to_str(successor)
#                 if successor_str not in previous_states:  # Check if the successor is a new state
#                     successors.append(successor)
#                     previous_states[successor_str] = 1  # Add the new state to the history

#     return successors

history = {}

ans = generate_successors(state)
print("intial state: \n", state, "\n")
print("Successors: ", len(ans))
for i in ans:
    print(i, "\n")


# # Second round of testing
# new_state = np.copy(ans[0])
# print("New intial state: \n", new_state, "\n")
# new_ans = generate_successors(new_state)
# print("Successors: ", len(new_ans))
# for i in new_ans:
#     print(i, "\n")




# # Third round of testing
# new_s = np.copy(new_ans[1])
# print("New intial state: \n", new_s, "\n")
# new_a = generate_successors(new_s)
# print("Successors: ", len(new_a))
# for i in new_a:
#     print(i, "\n")

# # Fourth round of testing
# new_state = np.copy(new_a[3])
# print("New intial state: \n", new_state, "\n")
# new_ans = generate_successors(new_state)
# print("Successors: ", len(new_ans))
# for i in new_ans:
#     print(i, "\n")
