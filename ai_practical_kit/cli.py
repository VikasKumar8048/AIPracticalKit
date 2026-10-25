"""Text menu for running and inspecting AIPracticalKit experiments."""

import importlib
from pathlib import Path
import shutil
import subprocess
import sys

SOURCE_DIR = Path(__file__).resolve().parent / "experiments"

EXPERIMENTS = [
    (1, "Simple Reflex Agent - Vacuum Cleaner", "vacuum_cleaner.py", "vacuum_cleaner"),
    (2, "A* Search - 8-Puzzle", "astar_8_puzzle.py", "astar_8_puzzle"),
    (3, "Alpha-Beta Pruning", "alpha_beta_pruning.py", "alpha_beta_pruning"),
    (4, "Tower of Hanoi using BFS", "tower_of_hanoi_bfs.py", "tower_of_hanoi_bfs"),
    (5, "Sudoku - Constraint Propagation and Backtracking", "sudoku_solver.py", "sudoku_solver"),
    (6, "Local Beam Search - TSP", "local_beam_tsp.py", "local_beam_tsp"),
    (7, "BFS - Robot Path Planning", "robot_path_bfs.py", "robot_path_bfs"),
    (8, "DFS - Maze Solving", "maze_dfs.py", "maze_dfs"),
    (9, "8-Queens using Backtracking", "eight_queens.py", "eight_queens"),
    (10, "Rule-Based Chatbot - Regex and AND", "rule_chatbot.py", "rule_chatbot"),
    (11, "Tic-Tac-Toe using Minimax", "tictactoe_minimax.py", "tictactoe_minimax"),
]


def _select_experiment():
    print("\nAI PRACTICAL KIT - EXPERIMENTS")
    for number, title, _, _ in EXPERIMENTS:
        print(str(number) + ". " + title)
    try:
        number = int(input("Experiment number (0 to cancel): ").strip())
    except ValueError:
        print("Please enter a number.")
        return None
    if number == 0:
        return None
    for item in EXPERIMENTS:
        if item[0] == number:
            return item
    print("Invalid experiment number.")
    return None


def _open_editor(path):
    editor = shutil.which("code")
    try:
        if editor:
            subprocess.Popen([editor, "--reuse-window", str(path)])
        elif sys.platform.startswith("win"):
            subprocess.Popen(["notepad.exe", str(path)])
        elif sys.platform == "darwin":
            subprocess.Popen(["open", "-t", str(path)])
        else:
            opener = shutil.which("xdg-open")
            if opener:
                subprocess.Popen([opener, str(path)])
            else:
                print("Open this source in your editor:\n" + str(path))
                return
        print("Opened source:", path.name)
    except OSError as error:
        print("Could not open the editor:", error)
        print("Source file:", path)


def _copy_source(path):
    source = path.read_text(encoding="utf-8")
    commands = []
    if sys.platform.startswith("win"):
        commands.append(["clip"])
    elif sys.platform == "darwin":
        commands.append(["pbcopy"])
    else:
        commands.extend([["wl-copy"], ["xclip", "-selection", "clipboard"],
                         ["xsel", "--clipboard", "--input"]])

    for command in commands:
        if shutil.which(command[0]):
            try:
                subprocess.run(command, input=source, text=True, check=True)
                print("Copied source to clipboard:", path.name)
                return
            except (OSError, subprocess.CalledProcessError):
                pass

    try:
        import tkinter
        window = tkinter.Tk()
        window.withdraw()
        window.clipboard_clear()
        window.clipboard_append(source)
        window.update()
        window.destroy()
        print("Copied source to clipboard:", path.name)
    except Exception:
        print("Clipboard copy is unavailable. Open this source and copy it manually:")
        print(path)


def main():
    """Run the installed text menu."""
    while True:
        print("\n" + "=" * 60)
        print("                AI PRACTICAL KIT")
        print("       Run algorithms or inspect full source code")
        print("=" * 60)
        print("1. Run an experiment")
        print("2. View full source code")
        print("3. Open source in an editor")
        print("4. Copy source code")
        print("5. Show import examples")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Good luck with your practical examinations!")
            return

        if choice == "5":
            print("\nfrom ai_practical_kit import solve_astar")
            print('result = solve_astar("123406758")')
            print('print(result["path"])')
            print("\nfrom ai_practical_kit import solve_8_queens")
            print("result = solve_8_queens()")
            print('print(result["total_solutions"])')
            print("\nfrom ai_practical_kit import respond")
            print('print(respond("Tell me about admission and fees"))')
            continue

        item = _select_experiment()
        if item is None:
            continue
        number, title, filename, module_name = item
        path = SOURCE_DIR / filename

        if choice == "1":
            module = importlib.import_module("ai_practical_kit.experiments." + module_name)
            try:
                module.run_cli()
            except (KeyboardInterrupt, EOFError):
                print("\nExperiment cancelled.")
        elif choice == "2":
            print("\n" + "=" * 72)
            print(title + " — FULL SOURCE")
            print("=" * 72)
            print(path.read_text(encoding="utf-8"))
            print("=" * 72)
        elif choice == "3":
            _open_editor(path)
        elif choice == "4":
            _copy_source(path)
        else:
            print("Invalid choice. Choose 0 to 5.")


if __name__ == "__main__":
    main()
