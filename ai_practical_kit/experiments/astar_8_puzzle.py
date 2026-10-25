"""Experiment 2: A* Search for the 8-Puzzle using Manhattan distance."""

import heapq

GOAL = "123456780"


def heuristic(state):
    """Sum of Manhattan distances; the blank ('0') is ignored."""
    distance = 0
    for index in range(9):
        if state[index] != "0":
            goal_index = int(state[index]) - 1
            distance += abs(index // 3 - goal_index // 3)
            distance += abs(index % 3 - goal_index % 3)
    return distance


def is_solvable(state):
    """For a 3x3 puzzle, the inversion count must be even."""
    numbers = [int(ch) for ch in state if ch != "0"]
    inversions = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1
    return inversions % 2 == 0


def solve_astar(start):
    """Solve a valid 8-puzzle string. Return path, moves and expanded count."""
    start = "".join(str(x) for x in start) if not isinstance(start, str) else start.strip().replace(" ", "")
    if len(start) != 9 or sorted(start) != list("012345678"):
        raise ValueError("State must contain digits 0 through 8 exactly once.")
    if not is_solvable(start):
        return {"found": False, "path": [], "moves": None, "expanded": 0}

    # Entries are (f, g, state); smallest f is removed first.
    open_queue = []
    heapq.heappush(open_queue, (heuristic(start), 0, start))
    best_g = {start: 0}
    parent = {start: None}
    expanded = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_queue:
        f, current_g, current = heapq.heappop(open_queue)
        if current_g != best_g.get(current):
            continue  # An older, worse queue entry.

        expanded += 1
        if current == GOAL:
            path = []
            state = current
            while state is not None:
                path.append(state)
                state = parent[state]
            path.reverse()
            return {"found": True, "path": path, "moves": len(path) - 1,
                    "expanded": expanded}

        blank = current.index("0")
        row = blank // 3
        col = blank % 3

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            if nr < 0 or nr >= 3 or nc < 0 or nc >= 3:
                continue

            new_blank = nr * 3 + nc
            chars = list(current)
            chars[blank], chars[new_blank] = chars[new_blank], chars[blank]
            next_state = "".join(chars)
            new_g = current_g + 1

            if new_g < best_g.get(next_state, 10**9):
                best_g[next_state] = new_g
                parent[next_state] = current
                heapq.heappush(open_queue,
                               (new_g + heuristic(next_state), new_g, next_state))

    return {"found": False, "path": [], "moves": None, "expanded": expanded}


def print_board(state):
    for i in range(9):
        print(("_" if state[i] == "0" else state[i]), end=" ")
        if i % 3 == 2:
            print()


def run_cli():
    print("\nEXPERIMENT 2: A* SEARCH FOR 8-PUZZLE")
    raw = input("Enter 9 digits (0 = blank), e.g. 1 2 3 4 0 6 7 5 8: ")
    start = "".join(raw.split())
    try:
        result = solve_astar(start)
    except ValueError as error:
        print("Input error:", error)
        return
    if not result["found"]:
        print("No solution exists for this puzzle.")
        return
    print("\nSolution path:")
    for step, state in enumerate(result["path"]):
        print("\nStep", step, "(g =", step, ", h =", heuristic(state),
              ", f =", step + heuristic(state), ")")
        print_board(state)
    print("Number of moves:", result["moves"])
    print("Nodes expanded:", result["expanded"])


if __name__ == "__main__":
    run_cli()
