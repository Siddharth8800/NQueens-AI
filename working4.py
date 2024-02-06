import numpy as np


def is_safe(board, row, col, n):
    # Check the row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    # base case: If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Print the board
            print(f"Placing a queen at row {i}, column {col}")
            print(np.array(board))
            print("\n")

            # recur to place rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # remove queen from board[i][col]
            print(f"No solution found by placing queen at row {i}, column {col}. Backtracking and trying next row.")
            board[i][col] = 0

    # If the queen cannot be placed in any row in
    # this column col then return false
    return False


def solve(n):
    board = [[0]*n for _ in range(n)]

    if not solve_n_queens(board, 0, n):
        print("Solution does not exist")
        return False

    print(np.array(board))
    return True


n = int(input("Enter the number of Queens: "))
solve(n)
    

    

    



