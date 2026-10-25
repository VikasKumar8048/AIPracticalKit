"""Small examples showing how to import and reuse AIPracticalKit functions."""

from ai_practical_kit import solve_astar, solve_8_queens, respond

# Example 1: Solve a simple 8-Puzzle (0 means blank).
result = solve_astar("123406758")
if result["found"]:
    print("A* moves:", result["moves"])
    print("A* path:", result["path"])

# Example 2: Get the first 8-Queens solution and count all solutions.
queens = solve_8_queens()
print("First 8-Queens solution:", queens["solution"])
print("Total 8-Queens solutions:", queens["total_solutions"])

# Example 3: Ask the rule-based chatbot a question.
print("Chatbot:", respond("Tell me about admission and fees"))
