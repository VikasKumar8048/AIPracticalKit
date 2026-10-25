"""Experiment 11: Tic-Tac-Toe game-playing agent using Minimax."""

WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def check_winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] != " " and board[a] == board[b] and board[b] == board[c]:
            return board[a]
    if " " in board:
        return " "
    return "D"


def minimax(board, is_max):
    result = check_winner(board)
    if result == "X":
        return 1
    if result == "O":
        return -1
    if result == "D":
        return 0

    if is_max:
        best = -2
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                if score > best:
                    best = score
        return best

    best = 2
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, True)
            board[i] = " "
            if score < best:
                best = score
    return best


def find_best_move(board):
    """Return the zero-based best move for X, or None if game is over."""
    if len(board) != 9:
        raise ValueError("Board must contain 9 cells.")
    if check_winner(board) != " ":
        return None

    best_score = -2
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


def display_board(board):
    for row in range(3):
        cells = []
        for col in range(3):
            index = row * 3 + col
            if board[index] == " ":
                cells.append(str(index + 1))
            else:
                cells.append(board[index])
        print(" | ".join(cells))
        if row < 2:
            print("---------")


def run_demo():
    board = ["X", "X", " ", "O", "O", " ", " ", " ", " "]
    print("\nInitial board (X = AI, O = opponent):")
    display_board(board)
    move = find_best_move(board)
    if move is None:
        print("No move available; the game has ended.")
        return
    print("\nBest move for AI:", move + 1)
    board[move] = "X"
    print("\nBoard after AI move:")
    display_board(board)
    print("Minimax score:", minimax(board, True))


def play_game():
    board = [" "] * 9
    print("\nTic-Tac-Toe: AI = X, You = O")
    while True:
        move = find_best_move(board)
        if move is not None:
            board[move] = "X"
            print("\nAI chooses:", move + 1)
            display_board(board)
        result = check_winner(board)
        if result == "X":
            print("AI wins!")
            break
        if result == "D":
            print("Draw!")
            break

        while True:
            try:
                position = int(input("Enter your move (1-9): "))
            except ValueError:
                print("Enter a number from 1 to 9.")
                continue
            if position >= 1 and position <= 9 and board[position - 1] == " ":
                break
            print("Invalid or occupied position. Try again.")
        board[position - 1] = "O"
        display_board(board)
        result = check_winner(board)
        if result == "O":
            print("You win!")
            break
        if result == "D":
            print("Draw!")
            break


def run_cli():
    print("\nEXPERIMENT 11: TIC-TAC-TOE USING MINIMAX")
    print("1. Demonstrate the best move (no human input)")
    print("2. Play against the AI")
    choice = input("Choose 1 or 2 [1]: ").strip()
    if choice == "2":
        play_game()
    else:
        run_demo()


if __name__ == "__main__":
    run_cli()
