import numpy as np
import queue

n = int(input("Enter n: "))
board = np.zeros((n, n), dtype=int)
closed = set()
temp = tuple(board.flatten())
closed.add(temp)

print("\n", board, "\n")
print(closed)
