board = [" " for _ in range(9)]


def display_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def is_draw():
    return " " not in board


def minimax(is_maximizing):
    # AI wins
    if check_winner("O"):
        return 1

    # Human wins
    if check_winner("X"):
        return -1

    # Draw
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def ai_move():
    best_score = -1000
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


# Main Game
print("TIC-TAC-TOE AI")
print("You = X")
print("AI = O")

while True:

    display_board()

    # Human move
    try:
        position = int(input("Enter your position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Enter a number between 1 and 9.")
            continue

        if board[position] != " ":
            print("Position already occupied!")
            continue

        board[position] = "X"

    except ValueError:
        print("Enter a valid number.")
        continue

    # Check human win
    if check_winner("X"):
        display_board()
        print("You Win!")
        break

    # Check draw
    if is_draw():
        display_board()
        print("Draw!")
        break

    # AI move
    print("AI is thinking...")
    ai_move()

    # Check AI win
    if check_winner("O"):
        display_board()
        print("AI Wins!")
        break

    # Check draw
    if is_draw():
        display_board()
        print("Draw!")
        break
