"""Desktop source browser for AIPracticalKit.

Launch with ``ai-practical-kit-gui`` or ``python -m ai_practical_kit.gui``.
Tkinter is part of many desktop Python installations; it is not a package dependency.
"""

from pathlib import Path
import shutil
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

SOURCE_DIR = Path(__file__).resolve().parent / "experiments"
EXPERIMENTS = [
    ("1. Simple Reflex Agent - Vacuum Cleaner", "vacuum_cleaner.py"),
    ("2. A* Search - 8-Puzzle", "astar_8_puzzle.py"),
    ("3. Alpha-Beta Pruning", "alpha_beta_pruning.py"),
    ("4. Tower of Hanoi using BFS", "tower_of_hanoi_bfs.py"),
    ("5. Sudoku - Constraint Propagation + Backtracking", "sudoku_solver.py"),
    ("6. Local Beam Search - TSP", "local_beam_tsp.py"),
    ("7. BFS - Robot Path Planning", "robot_path_bfs.py"),
    ("8. DFS - Maze Solving", "maze_dfs.py"),
    ("9. 8-Queens using Backtracking", "eight_queens.py"),
    ("10. Rule-Based Chatbot - Regex and AND", "rule_chatbot.py"),
    ("11. Tic-Tac-Toe using Minimax", "tictactoe_minimax.py"),
]


class AIPracticalKitApp:
    def __init__(self, root):
        self.root = root
        root.title("AIPracticalKit - Source Browser")
        root.geometry("1120x740")
        root.minsize(850, 550)

        tk.Label(root, text="AIPracticalKit", font=("Segoe UI", 18, "bold")).pack(
            anchor="w", padx=12, pady=(10, 0))
        tk.Label(root, text=(
            "Select an experiment to preview its full code, run it, open it in an editor, "
            "copy it, or save a copy."), font=("Segoe UI", 10)).pack(
            anchor="w", padx=12, pady=(0, 10))

        body = tk.Frame(root)
        body.pack(fill="both", expand=True, padx=12, pady=4)
        left = tk.Frame(body, width=310)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)
        tk.Label(left, text="11 experiments", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        self.listbox = tk.Listbox(left, font=("Segoe UI", 10), exportselection=False)
        self.listbox.pack(fill="both", expand=True, pady=(5, 8))
        for title, _ in EXPERIMENTS:
            self.listbox.insert(tk.END, title)
        self.listbox.bind("<<ListboxSelect>>", self.show_source)

        buttons = tk.Frame(left)
        buttons.pack(fill="x", pady=(0, 8))
        tk.Button(buttons, text="Run selected experiment", command=self.run_selected).pack(fill="x", pady=2)
        tk.Button(buttons, text="Open source in editor", command=self.open_editor).pack(fill="x", pady=2)
        tk.Button(buttons, text="Copy source to clipboard", command=self.copy_source).pack(fill="x", pady=2)
        tk.Button(buttons, text="Save a copy of source...", command=self.save_source).pack(fill="x", pady=2)

        right = tk.Frame(body)
        right.pack(side="left", fill="both", expand=True, padx=(12, 0))
        tk.Label(right, text="Full source code", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        code_frame = tk.Frame(right)
        code_frame.pack(fill="both", expand=True, pady=(5, 0))
        self.code = tk.Text(code_frame, wrap="none", font=("Consolas", 10), undo=False)
        vertical = tk.Scrollbar(code_frame, orient="vertical", command=self.code.yview)
        horizontal = tk.Scrollbar(code_frame, orient="horizontal", command=self.code.xview)
        self.code.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)
        self.code.grid(row=0, column=0, sticky="nsew")
        vertical.grid(row=0, column=1, sticky="ns")
        horizontal.grid(row=1, column=0, sticky="ew")
        code_frame.rowconfigure(0, weight=1)
        code_frame.columnconfigure(0, weight=1)
        self.status = tk.StringVar(value="Select an experiment.")
        tk.Label(root, textvariable=self.status, anchor="w", relief="sunken").pack(fill="x", side="bottom")
        self.listbox.selection_set(0)
        self.show_source()

    def selected_path(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Choose experiment", "Select an experiment first.")
            return None
        return SOURCE_DIR / EXPERIMENTS[selected[0]][1]

    def show_source(self, event=None):
        path = self.selected_path()
        if path is None:
            return
        try:
            source = path.read_text(encoding="utf-8")
        except OSError as error:
            messagebox.showerror("Cannot read source", str(error))
            return
        self.code.delete("1.0", tk.END)
        self.code.insert("1.0", source)
        self.code.mark_set("insert", "1.0")
        self.status.set("Source loaded: " + path.name + " | " + str(len(source.splitlines())) + " lines")

    def open_editor(self):
        path = self.selected_path()
        if path is None:
            return
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
                if opener is None:
                    messagebox.showinfo("Source file", "Source path:\n" + str(path))
                    return
                subprocess.Popen([opener, str(path)])
            self.status.set("Opened source: " + path.name)
        except OSError as error:
            messagebox.showerror("Could not open editor", str(error) + "\n\n" + str(path))

    def copy_source(self):
        try:
            source = self.code.get("1.0", "end-1c")
            self.root.clipboard_clear()
            self.root.clipboard_append(source)
            self.root.update()
            self.status.set("Copied source code to clipboard.")
        except tk.TclError as error:
            messagebox.showerror("Clipboard error", str(error))

    def save_source(self):
        path = self.selected_path()
        if path is None:
            return
        target = filedialog.asksaveasfilename(
            title="Save source as", initialfile=path.name, defaultextension=".py",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")])
        if not target:
            return
        try:
            Path(target).write_text(self.code.get("1.0", "end-1c"), encoding="utf-8")
            self.status.set("Saved source copy: " + target)
        except OSError as error:
            messagebox.showerror("Save error", str(error))

    def run_selected(self):
        path = self.selected_path()
        if path is None:
            return
        try:
            if sys.platform.startswith("win"):
                subprocess.Popen([sys.executable, str(path)], cwd=str(path.parent),
                                 creationflags=getattr(subprocess, "CREATE_NEW_CONSOLE", 0))
                self.status.set("Started in a separate console: " + path.name)
            else:
                subprocess.Popen([sys.executable, str(path)], cwd=str(path.parent))
                self.status.set("Started experiment process: " + path.name)
        except OSError as error:
            messagebox.showerror("Run error", str(error))


def main():
    root = tk.Tk()
    AIPracticalKitApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
