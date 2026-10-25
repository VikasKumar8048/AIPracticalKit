"""Experiment 3: Alpha-Beta Pruning on a depth-3 binary game tree."""

INFINITY = 10**9
DEFAULT_LEAVES = [3, 5, 6, 9, 1, 2, 0, -1]
INTERNAL_NAMES = "ABCDEFG"


def solve_alpha_beta(leaf_values=None):
    """Return minimax value, root branch, evaluated leaves and pruned branches."""
    if leaf_values is None:
        leaf_values = DEFAULT_LEAVES[:]
    leaf_values = list(leaf_values)
    if len(leaf_values) != 8:
        raise ValueError("Enter exactly 8 leaf values.")

    evaluated = 0
    pruned = []
    best_root_branch = None

    def node_name(node_index):
        if node_index < 7:
            return INTERNAL_NAMES[node_index]
        return str(leaf_values[node_index - 7])

    def search(node, depth, is_max, alpha, beta):
        nonlocal evaluated, best_root_branch

        if depth == 3:
            evaluated += 1
            return leaf_values[node - 7]

        if is_max:
            best = -INFINITY
        else:
            best = INFINITY

        for child_number in range(2):
            child = 2 * node + 1 + child_number
            score = search(child, depth + 1, not is_max, alpha, beta)

            if is_max:
                if score > best:
                    best = score
                    if node == 0:
                        best_root_branch = node_name(child)
                if best > alpha:
                    alpha = best
            else:
                if score < best:
                    best = score
                if best < beta:
                    beta = best

            if alpha >= beta:
                if child_number == 0:
                    skipped = 2 * node + 2
                    if depth + 1 == 3:
                        pruned.append("leaf " + node_name(skipped))
                    else:
                        pruned.append("subtree " + node_name(skipped))
                break

        return best

    value = search(0, 0, True, -INFINITY, INFINITY)
    return {"value": value, "best_branch": best_root_branch,
            "leaves_evaluated": evaluated, "pruned": pruned,
            "leaf_values": leaf_values}


def run_cli():
    print("\nEXPERIMENT 3: ALPHA-BETA PRUNING")
    print("Enter 8 leaf values from left to right, or press Enter for the practical example.")
    raw = input("Leaf values [3 5 6 9 1 2 0 -1]: ").strip()
    try:
        values = DEFAULT_LEAVES if raw == "" else [int(x) for x in raw.split()]
        result = solve_alpha_beta(values)
    except ValueError as error:
        print("Input error:", error)
        return
    print("Minimax value at root:", result["value"])
    print("Best branch for MAX:", result["best_branch"])
    print("Leaves evaluated:", result["leaves_evaluated"], "out of 8")
    if result["pruned"]:
        print("Pruned:", ", ".join(result["pruned"]))
    else:
        print("Pruned: none")


if __name__ == "__main__":
    run_cli()
