"""Experiment 8: DFS for Maze Solving."""


def solve_maze_dfs(maze):
    """Find a path from S to E by DFS; return path and a marked maze."""
    if not maze or not maze[0]:
        raise ValueError("Maze cannot be empty.")
    rows = len(maze)
    cols = len(maze[0])
    if any(len(row) != cols for row in maze):
        raise ValueError("All maze rows must have the same length.")

    start = None
    goal = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                if start is not None:
                    raise ValueError("Maze must contain exactly one S.")
                start = (r, c)
            elif maze[r][c] == "E":
                if goal is not None:
                    raise ValueError("Maze must contain exactly one E.")
                goal = (r, c)
    if start is None or goal is None:
        raise ValueError("Maze must contain one S (start) and one E (exit).")

    visited = set()
    path = []
    # Same order as the practical: Right, Down, Left, Up.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if maze[r][c] == "#" or (r, c) in visited:
            return False

        visited.add((r, c))
        path.append((r, c))
        if (r, c) == goal:
            return True

        for dr, dc in directions:
            if dfs(r + dr, c + dc):
                return True

        path.pop()  # Dead end: remove this cell from the current path.
        return False

    found = dfs(start[0], start[1])
    if not found:
        return {"found": False, "path": [], "maze": list(maze),
                "visited_count": len(visited)}

    marked = [list(row) for row in maze]
    for r, c in path:
        if marked[r][c] == ".":
            marked[r][c] = "*"
    return {"found": True, "path": path,
            "maze": ["".join(row) for row in marked],
            "visited_count": len(visited)}


def run_cli():
    print("\nEXPERIMENT 8: DFS MAZE SOLVER")
    try:
        rows, cols = [int(x) for x in input("Enter rows and columns: ").split()]
        if rows < 1 or cols < 1 or rows > 50 or cols > 50:
            raise ValueError("Rows and columns must be between 1 and 50.")
        print("Enter each maze row using S=start, E=exit, #=wall, .=free:")
        maze = [input().strip() for _ in range(rows)]
        if any(len(row) != cols for row in maze):
            raise ValueError("Each row must contain exactly the given number of columns.")
        result = solve_maze_dfs(maze)
    except ValueError as error:
        print("Input error:", error)
        return

    if not result["found"]:
        print("No path exists in the maze.")
        return
    print("\nPath found (DFS does not guarantee shortest path):")
    for r, c in result["path"]:
        print("(" + str(r + 1) + "," + str(c + 1) + ")", end=" ")
    print("\n\nMaze with path:")
    for row in result["maze"]:
        print(" ".join(row))


if __name__ == "__main__":
    run_cli()
