"""Quick smoke tests for all 11 AIPracticalKit algorithms."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ai_practical_kit import (
    solve_vacuum, solve_astar, solve_alpha_beta, solve_hanoi_bfs,
    solve_sudoku, local_beam_tsp, solve_robot_bfs, solve_maze_dfs,
    solve_8_queens, respond, find_best_move,
)

assert solve_vacuum("D", "C", "A")["room_a"] == "C"
assert solve_astar("123406758")["moves"] == 2
assert solve_alpha_beta()["value"] == 5
assert solve_hanoi_bfs(3)["number_of_moves"] == 7

sudoku = [list(map(int, row)) for row in [
    "530070000", "600195000", "098000060", "800060003", "400803001",
    "700020006", "060000280", "000419005", "000080079",
]]
solution = solve_sudoku(sudoku)
assert solution is not None
assert all(sorted(row) == list(range(1, 10)) for row in solution)

distance = [
    [0, 10, 15, 20], [10, 0, 35, 25],
    [15, 35, 0, 30], [20, 25, 30, 0],
]
tsp = local_beam_tsp(distance, beam_width=2, max_iterations=5)
assert len(tsp["tour"]) == 4 and tsp["cost"] == 80

robot_maze = ["S...#", ".#.##", ".#...", ".###.", "...#G"]
assert solve_robot_bfs(robot_maze)["moves"] == 8

dfs_maze = ["S.#...", ".##.#.", "....#.", ".##...", "...#.E"]
assert solve_maze_dfs(dfs_maze)["found"]
assert solve_8_queens()["total_solutions"] == 92
assert "AND" in respond("Tell me about admission and fees")
assert find_best_move(["X", "X", " ", "O", "O", " ", " ", " ", " "]) == 2

print("All 11 AIPracticalKit smoke tests passed.")
