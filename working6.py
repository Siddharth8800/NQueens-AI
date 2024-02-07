import numpy as np


def manhattan_distance(i, j, n):
    """
    Calculate the Manhattan distance between two queens.

    Args:
        i (int): Row index of the first queen.
        j (int): Column index of the first queen.
        n (int): Size of the chessboard.

    Returns:
        int: Manhattan distance between the two queens.
    """
    return abs(i - j)


def calculate_heuristic(state, n):
    """
    Calculate the heuristic value for a given state.

    Args:
        state (np.ndarray): Current state of the chessboard.
        n (int): Size of the chessboard.

    Returns:
        int: Heuristic value for the state.
    """
    total_conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Check for conflicts in the same row
            if state[i] == state[j]:
                total_conflicts += 1

            # Check for conflicts in the same diagonal
            if abs(i - j) == abs(state[i] - state[j]):
                total_conflicts += 1

    return total_conflicts


def is_valid_move(state, i, j, n):
    """
    Check if a move is valid.

    Args:
        state (np.ndarray): Current state of the chessboard.
        i (int): Row index of the queen to move.
        j (int): Column index of the new position.
        n (int): Size of the chessboard.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Check if the queen is already in the new position
    if state[i] == j:
        return False

    # Check if there are conflicts in the same row or diagonal
    for k in range(n):
        if k != i and (state[k] == j or abs(k - i) == abs(state[k] - j)):
            return False

    return True


def a_star_search(n):
    """
    Solve the N-Queens problem using A* search.

    Args:
        n (int): Size of the chessboard.

    Returns:
        np.ndarray: Solution state with queens placed on the chessboard.
        list: List of moves made to reach the solution.
    """
    initial_state = np.zeros(n, dtype=int)
    frontier = [(initial_state, 0, calculate_heuristic(initial_state, n))]
    explored = set()

    while frontier:
        # Sort the frontier by f-score (total cost + heuristic)
        frontier.sort(key=lambda x: x[1] + x[2])
        current_state, current_cost, current_heuristic = frontier.pop(0)
        explored.add(tuple(current_state))

        # Check if goal state is reached
        if np.all(current_state != -1):
            return current_state, []

        # Generate possible moves
        for i in range(n):
            if current_state[i] == -1:
                for j in range(n):
                    if is_valid_move(current_state, i, j, n):
                        new_state = current_state.copy()
                        new_state[i] = j
                        new_cost = current_cost + 1
                        new_heuristic = calculate_heuristic(new_state, n)
                        frontier.append((new_state, new_cost, new_heuristic))

    return None, None


def solve_n_queens(n):
    """
    Solve the N-Queens problem and print the moves and total move count.

    Args:
        n (int): Size of the chessboard.
    """
    solution_state, moves = a_star_search(n)

    if solution_state is not None:
        print("Solution:")
        print(solution_state)
        print("Moves:")
        for move in moves:
            print(move)
        print("Total moves:", len(moves))
    else:
        print("No solution found.")

# Example usage
n = 4
solve_n_queens(n)
