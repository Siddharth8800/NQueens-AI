import numpy as np

class StateGenerator:
    def __init__(self, n):
        self.n = n
        self.states = {}

    def generate_state(self):
        state = np.zeros((self.n, self.n), dtype=int)
        for i in range(self.n):
            state[i, i] = 1

        # Check if the state has already been generated
        key = tuple(state.flatten())
        if key not in self.states:
            self.states[key] = state
            return state.copy()
        else:
            # Move the 1 to the right by 1
            state[state == 1] = 0
            # Handle edge case for single row matrix
            if self.n == 1:
                state[0, 0] = 1
                return state.copy()
            elif state[0, -1] == 0:
                state[0, -1] = 1
            else:
                # Wrap around to the beginning
                state[0, 0] = 1
            return state.copy()

# Example usage
generator = StateGenerator(3)
state1 = generator.generate_state()
state2 = generator.generate_state()
state3 = generator.generate_state()

print(state1)
print()
print(state2)
print()
print(state3)




# import numpy as np

# class StateGenerator:
#     def __init__(self, n):
#         self.n = n
#         self.current_state = None

#     def generate_state(self):
#         """
#         Generates a new state by moving the 1 in the previous state.

#         Returns:
#             numpy.ndarray: The new state matrix.
#         """
#         if self.current_state is None:
#             # Start with a state with the 1 on the main diagonal
#             state = np.zeros((self.n, self.n), dtype=int)
#             for i in range(self.n):
#                 state[i, i] = 1
#             self.current_state = state
#         else:
#             # Move the 1 from the previous state
#             prev_state = self.current_state
#             new_state = np.zeros_like(prev_state)
#             new_state[:, prev_state.argmax(axis=1)] = 1
#             self.current_state = new_state

#         return self.current_state.copy()

# # Example usage
# generator = StateGenerator(4)
# for _ in range(5):
#     state = generator.generate_state()
#     print(state)
#     print()


# class StateGenerator:
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

                



                        


        

