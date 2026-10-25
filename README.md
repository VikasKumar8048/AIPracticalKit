# AIPracticalKit — Offline AI Laboratory Practical Library

AIPracticalKit packages the 11 AI practicals as reusable Python functions and includes each complete `.py` implementation. It also provides a text menu and a desktop source browser so a student can run an experiment, inspect its code, copy it, or save a separate copy.

**No third-party runtime dependencies. No internet is needed after you have downloaded the wheel or ZIP.** Python must already be installed on the computer. The graphical source browser uses Tkinter, which is included with most desktop Python installations.

## Included experiments

1. Simple Reflex Agent — Vacuum Cleaner World
2. A* Search — 8-Puzzle using Manhattan distance
3. Alpha-Beta Pruning — binary game tree
4. Tower of Hanoi — BFS state-space search
5. Sudoku — constraint propagation and backtracking
6. Local Beam Search — Traveling Salesman Problem
7. BFS — Robot Path Planning
8. DFS — Maze Solving
9. 8-Queens — backtracking and solution counting
10. Rule-Based Chatbot — regular expressions, random responses and AND rule
11. Tic-Tac-Toe — Minimax, demonstration mode and optional human-vs-AI mode

## Recommended offline installation on Windows

### Method A — install the wheel (works without internet)

1. Extract the `AIPracticalKit_Offline_Install.zip` package.
2. Open the extracted folder. It contains `dist/ai_practical_kit-1.1.0-py3-none-any.whl`.
3. Double-click `INSTALL_OFFLINE.bat`, or open PowerShell in that folder and run:

   ```powershell
   py -m pip install --no-index --no-deps --upgrade .\dist\ai_practical_kit-1.1.0-py3-none-any.whl
   ```

   If the `py` launcher is unavailable, use `python -m pip` instead.
4. In VS Code, select the same Python interpreter that you used for installation.
5. Test the installation:

   ```powershell
   py -c "from ai_practical_kit import solve_astar; print(solve_astar('123406758')['moves'])"
   ```

   The expected number of moves is `2`.

The wheel is pure Python and the project has no third-party runtime dependencies. `--no-index` tells pip not to contact a package index; `--no-deps` prevents dependency downloads.

### Method B — use the source folder without installing

Extract the full source ZIP, open the `AIPracticalKit` folder in VS Code, and run:

```powershell
py app.py
```

For a text menu, run:

```powershell
py run.py
```

This source-folder method also works offline and leaves the package uninstalled.

## Open the source browser after installing the wheel

After the wheel is installed, launch:

```powershell
ai-practical-kit-gui
```

Or run the module directly:

```powershell
py -m ai_practical_kit.gui
```

The GUI lets you select an experiment, view its entire source, run it, open its `.py` file in an editor, copy its source, or save a separate copy. If VS Code's `code` command is configured, the GUI opens the selected source in VS Code; otherwise, it uses a system text editor where available.

For the terminal menu, use:

```powershell
ai-practical-kit
```

or:

```powershell
py -m ai_practical_kit.cli
```

## Import individual algorithms into your own file

After installing the wheel, you can import the functions from any working directory using the same Python interpreter.

### A* Search for 8-Puzzle

```python
from ai_practical_kit import solve_astar

result = solve_astar("123406758")
print("Found:", result["found"])
print("Moves:", result["moves"])
print("Path:", result["path"])
```

### 8-Queens

```python
from ai_practical_kit import solve_8_queens

result = solve_8_queens()
print("First solution:", result["solution"])
print("Total solutions:", result["total_solutions"])
```

### Rule-based chatbot

```python
from ai_practical_kit import respond

print(respond("hello"))
print(respond("Tell me about admission and fees"))
```

### Other exported functions

```python
from ai_practical_kit import (
    solve_vacuum,
    solve_alpha_beta,
    solve_hanoi_bfs,
    solve_sudoku,
    local_beam_tsp,
    solve_robot_bfs,
    solve_maze_dfs,
    find_best_move,
    minimax,
)
```

Read `ai_practical_kit/experiments/` in the source ZIP or select an experiment in the source browser to see full implementations and exact inputs.

## Test the package

From the source project directory, run:

```powershell
py tests\smoke_test.py
```

Expected final line:

```text
All 11 AIPracticalKit smoke tests passed.
```

## Publishing to PyPI later (optional)

Offline installation does not require PyPI. If you later decide to publish the package for public installation, use `PUBLISH_TO_PYPI.md`. Publishing requires internet access, a PyPI account, and a package name that is available. This project is built locally; it has **not** been uploaded to PyPI by this ZIP.

## Notes

- The package is designed for study and practical examinations, not as a highly optimized production solver.
- A* validates the 8-puzzle state and checks parity before searching.
- BFS finds a shortest path when every move has equal cost. DFS finds a path but does not guarantee the shortest one.
- Local Beam Search is a heuristic and does not guarantee a globally optimal TSP tour.
- Alpha-Beta Pruning and Minimax evaluate the supplied game tree or board.
- Sudoku applies constraint propagation before recursive backtracking.
- The package distribution name is `ai-practical-kit`; the import name is `ai_practical_kit`.
