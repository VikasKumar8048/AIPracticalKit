"""Experiment 4: Tower of Hanoi solved by BFS over legal states."""

from collections import deque

PEG_NAMES = "ABC"


def solve_hanoi_bfs(number_of_disks):
    """Return shortest sequence of moves and the number of explored states.

    State is a tuple where state[d] is the peg index (0=A, 1=B, 2=C)
    holding disk d. Disk 0 is the smallest disk.
    """
    if not isinstance(number_of_disks, int) or number_of_disks < 1 or number_of_disks > 8:
        raise ValueError("Number of disks must be between 1 and 8.")

    start = tuple(0 for _ in range(number_of_disks))
    goal = tuple(2 for _ in range(number_of_disks))
    queue = deque([start])
    parent = {start: None}
    move_to_state = {}

    while queue:
        current = queue.popleft()
        if current == goal:
            break

        # Find the top (smallest numbered) disk on each peg.
        top = [-1, -1, -1]
        for disk in range(number_of_disks):
            peg = current[disk]
            if top[peg] == -1:
                top[peg] = disk

        for source in range(3):
            disk = top[source]
            if disk == -1:
                continue

            for destination in range(3):
                if source == destination:
                    continue

                destination_top = top[destination]
                # A larger disk cannot be placed on a smaller one.
                if destination_top != -1 and disk > destination_top:
                    continue

                next_state = list(current)
                next_state[disk] = destination
                next_state = tuple(next_state)

                if next_state not in parent:
                    parent[next_state] = current
                    move_to_state[next_state] = (
                        disk + 1, PEG_NAMES[source], PEG_NAMES[destination]
                    )
                    queue.append(next_state)

    if goal not in parent:
        return {"found": False, "moves": [], "states_explored": len(parent)}

    states = []
    moves = []
    state = goal
    while state is not None:
        states.append(state)
        if state in move_to_state:
            moves.append(move_to_state[state])
        state = parent[state]
    states.reverse()
    moves.reverse()

    return {"found": True, "states": states, "moves": moves,
            "number_of_moves": len(moves), "states_explored": len(parent)}


def run_cli():
    print("\nEXPERIMENT 4: TOWER OF HANOI USING BFS")
    try:
        n = int(input("Enter number of disks (1-8): "))
        result = solve_hanoi_bfs(n)
    except ValueError as error:
        print("Input error:", error)
        return

    if not result["found"]:
        print("No solution found.")
        return
    if not result["moves"]:
        print("No moves needed.")
    for step, move in enumerate(result["moves"], 1):
        disk, source, destination = move
        print("Step", step, ": Move disk", disk, "from", source, "to", destination)
    print("Total moves:", result["number_of_moves"])
    print("States explored:", result["states_explored"])


if __name__ == "__main__":
    run_cli()
