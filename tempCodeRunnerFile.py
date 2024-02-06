class StateGenerator:
#     def __init__(self, n):
#         self.n = n
#         self.states = {}
#         self.current_state = None

#     import numpy as np

#     def check_valid_state(state):
#         # Check if each row has exactly one 1
#         if not np.all(np.sum(state, axis=1) == 1):
#             return False

#         # Check if the 1 in each row can move to the next column
#         for i in range(state.shape[0]):
#             # Handle edge case for the last column
#             if i == state.shape[0] - 1:
#                 if state[i, 0] == 1:
#                     return False
#             else:
#                 if state[i, i + 1] == 1:
#                     return False

#         return True


    
#     def generate_states(self, state):
#         temp_state = np.copy(state)
#         for i in range (self.n):
#             for j in range (self.n):
#                 if temp_state[i][j] == 1:
#                     temp_state[i][j] = 0
#                     temp_state[i][j + 1 % self.n] = 1
#                     key = tuple(temp_state.flatten())
#                     if key not in self.states:
#                         self.states[key] = temp_state
#                     else:
#                         continue

                