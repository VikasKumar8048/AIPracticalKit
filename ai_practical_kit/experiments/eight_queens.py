"""Experiment 9: Backtracking for the 8-Queens constraint problem."""

SIZE = 8


def solve_8_queens():
    """Return the first solution and total number of solutions (92)."""
    board = [-1] * SIZE
    first_solution = None
    solution_count = 0

    def is_safe(row, col):
        for previous_row in range(row):
            if board[previous_row] == col:
                return False
            if abs(board[previous_row] - col) == abs(previous_row - row):
                return False
        return True

    def solve(row):
        nonlocal first_solution, solution_count
        if row == SIZE:
            solution_count += 1
            if first_solution is None:
                first_solution = board[:]
            return

        for col in range(SIZE):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1  # Backtrack and try another column.

    solve(0)
    return {"solution": first_solution, "total_solutions": solution_count}


def run_cli():
    print("\nEXPERIMENT 9: 8-QUEENS USING BACKTRACKING")
    result = solve_8_queens()
    board = result["solution"]
    if board is None:
        print("No solution exists.")
        return

    print("First solution (Q = queen, . = empty):")
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print("Queen positions (row, column; numbering starts at 1):")
    for row in range(SIZE):
        print("Queen", row + 1, ": (", row + 1, ", ", board[row] + 1, ")", sep="")
    print("Total solutions:", result["total_solutions"])


if __name__ == "__main__":
    run_cli()
