"""Experiment 7: BFS for Robot Path Planning on a grid."""

from collections import deque


def solve_robot_bfs(maze):
    """Find a shortest path in a grid containing S, G, # and . characters."""
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
            elif maze[r][c] == "G":
                if goal is not None:
                    raise ValueError("Maze must contain exactly one G.")
                goal = (r, c)
    if start is None or goal is None:
        raise ValueError("Maze must contain one S (start) and one G (goal).")

    queue = deque([start])
    parent = {start: None}
    distance = {start: 0}
    # Same direction order as the practical: Down, Right, Up, Left.
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for dr, dc in directions:
            nr = current[0] + dr
            nc = current[1] + dc
            next_cell = (nr, nc)
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if maze[nr][nc] == "#" or next_cell in parent:
                continue
            parent[next_cell] = current
            distance[next_cell] = distance[current] + 1
            queue.append(next_cell)

    if goal not in parent:
        return {"found": False, "path": [], "moves": None, "maze": list(maze)}

    path = []
    cell = goal
    while cell is not None:
        path.append(cell)
        cell = parent[cell]
    path.reverse()

    marked = [list(row) for row in maze]
    for r, c in path:
        if marked[r][c] == ".":
            marked[r][c] = "*"
    return {"found": True, "path": path, "moves": distance[goal],
            "maze": ["".join(row) for row in marked]}


def run_cli():
    print("\nEXPERIMENT 7: BFS ROBOT PATH PLANNING")
    try:
        rows, cols = [int(x) for x in input("Enter rows and columns: ").split()]
        if rows < 1 or cols < 1 or rows > 50 or cols > 50:
            raise ValueError("Rows and columns must be between 1 and 50.")
        print("Enter each maze row using S=start, G=goal, #=wall, .=free:")
        maze = [input().strip() for _ in range(rows)]
        if any(len(row) != cols for row in maze):
            raise ValueError("Each row must contain exactly the given number of columns.")
        result = solve_robot_bfs(maze)
    except ValueError as error:
        print("Input error:", error)
        return

    if not result["found"]:
        print("No path exists from S to G.")
        return
    print("\nShortest path (1-based coordinates):")
    print(" -> ".join("(" + str(r + 1) + "," + str(c + 1) + ")"
                      for r, c in result["path"]))
    print("Shortest path length:", result["moves"], "moves")
    print("\nFinal path grid:")
    for row in result["maze"]:
        print(" ".join(row))


if __name__ == "__main__":
    run_cli()
