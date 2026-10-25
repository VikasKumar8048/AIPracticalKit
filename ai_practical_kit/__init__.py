"""AIPracticalKit: reusable, beginner-friendly AI practical algorithms."""

from .experiments.vacuum_cleaner import solve_vacuum
from .experiments.astar_8_puzzle import solve_astar, heuristic
from .experiments.alpha_beta_pruning import solve_alpha_beta
from .experiments.tower_of_hanoi_bfs import solve_hanoi_bfs
from .experiments.sudoku_solver import solve_sudoku
from .experiments.local_beam_tsp import local_beam_tsp, tour_cost
from .experiments.robot_path_bfs import solve_robot_bfs
from .experiments.maze_dfs import solve_maze_dfs
from .experiments.eight_queens import solve_8_queens
from .experiments.rule_chatbot import respond
from .experiments.tictactoe_minimax import find_best_move, minimax

__version__ = "1.1.0"

__all__ = [
    "solve_vacuum", "solve_astar", "heuristic", "solve_alpha_beta",
    "solve_hanoi_bfs", "solve_sudoku", "local_beam_tsp", "tour_cost",
    "solve_robot_bfs", "solve_maze_dfs", "solve_8_queens", "respond",
    "find_best_move", "minimax",
]
