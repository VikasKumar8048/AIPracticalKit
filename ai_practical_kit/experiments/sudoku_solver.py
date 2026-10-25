"""Experiment 5: Sudoku solver using constraint propagation and backtracking."""


def is_safe(grid, row, col, number):
    """Return True if number does not repeat in its row, column or 3x3 box."""
    for i in range(9):
        if grid[row][i] == number:
            return False
        if grid[i][col] == number:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == number:
                return False
    return True


def valid_initial_grid(grid):
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        return False
    for row in range(9):
        for col in range(9):
            number = grid[row][col]
            if not isinstance(number, int) or number < 0 or number > 9:
                return False
            if number != 0:
                grid[row][col] = 0
                safe = is_safe(grid, row, col, number)
                grid[row][col] = number
                if not safe:
                    return False
    return True


def propagate(grid):
    """Repeatedly fill empty cells having exactly one legal candidate."""
    changed = True
    while changed:
        changed = False
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    candidates = []
                    for number in range(1, 10):
                        if is_safe(grid, row, col, number):
                            candidates.append(number)
                    if len(candidates) == 0:
                        return False
                    if len(candidates) == 1:
                        grid[row][col] = candidates[0]
                        changed = True
    return True


def solve_sudoku(puzzle):
    """Return a solved 9x9 grid, or None when no solution exists."""
    if not valid_initial_grid(puzzle):
        return None

    def solve(current_grid):
        # Work on a copy so a failed guess cannot damage the previous state.
        grid = [row[:] for row in current_grid]

        if not propagate(grid):
            return None

        empty_row = -1
        empty_col = -1
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    empty_row = row
                    empty_col = col
                    break
            if empty_row != -1:
                break

        if empty_row == -1:
            return grid

        for number in range(1, 10):
            if is_safe(grid, empty_row, empty_col, number):
                next_grid = [row[:] for row in grid]
                next_grid[empty_row][empty_col] = number
                answer = solve(next_grid)
                if answer is not None:
                    return answer
        return None

    return solve(puzzle)


def print_grid(grid):
    for row in range(9):
        if row in (3, 6):
            print("------+-------+------")
        for col in range(9):
            if col in (3, 6):
                print("|", end=" ")
            print(grid[row][col], end=" ")
        print()


def run_cli():
    print("\nEXPERIMENT 5: SUDOKU (CONSTRAINT PROPAGATION + BACKTRACKING)")
    print("Enter 9 rows, using 0 for empty cells. Example: 530070000")
    grid = []
    try:
        for _ in range(9):
            line = input().strip()
            if " " in line:
                row = [int(x) for x in line.split()]
            else:
                row = [int(ch) for ch in line]
            if len(row) != 9:
                raise ValueError("Each row must contain 9 digits.")
            grid.append(row)
    except ValueError as error:
        print("Input error:", error)
        return

    print("\nInitial Sudoku:")
    print_grid(grid)
    answer = solve_sudoku(grid)
    if answer is None:
        print("No solution exists or the starting grid is invalid.")
    else:
        print("\nSolved Sudoku:")
        print_grid(answer)


if __name__ == "__main__":
    run_cli()
