# 1. Name:
#      Caleb Barzee
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The assignment went okay. I really felt like some of the stuff was unnecessary,
#      or even bad programming practice (for instance the global variable). The hardest part
#      was probably revising some of the previously written code to be more concise.
# 5. How long did it take for you to complete the assignment?
#      3 hours
import os
import json


def initialize_blank_board():
    board_state = {
        "board": [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " "],
        "turn_count": 0
    }
    return board_state


def read_board():
    """Read the previously existing board from the file if it exists."""
    with open("tic_tac_toe/board.json", "r") as board_file:
        text = board_file.read()
        # print(text)
        board_state = json.loads(text)

    return board_state


def save_board(board_state):
    """Save the current game to a file."""
    with open("tic_tac_toe/board.json", "w") as board_file:
        board_file.write(json.dumps(board_state))


def display_board(board):
    """Display a Tic-Tac-Toe board on the screen in a user-friendly way."""
    print(
        f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(
        f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(
        f" {board[6]} | {board[7]} | {board[8]} \n")


def determine_turn(turn_count):
    """Determine whose turn it is."""
    if turn_count % 2 == 0:
        return "O"
    else:
        return "X"


def play_game(board_state):
    """Play the game of Tic-Tac-Toe."""
    # Put game play code here.
    # print(board_state)
    while True:
        print("The current board is:")
        display_board(board_state["board"])
        board_state["turn_count"] += 1
        response = input()
        if response == "q":
            return board_state
        index = int(response) - 1
        board_state["board"][index] = determine_turn(
            board_state["turn_count"])
        if game_done(board_state["board"]):
            display_board(board_state["board"])
            board_state = initialize_blank_board()
            return board_state


def game_done(board, message=True):
    """Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. """
# Why would we ever desire to hide the results from the user?

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != " " and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != " " and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != " " and (board[0] == board[4] == board[8] or
                            board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == " ":
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    return False


def main():
    # checking file path
    # directory = os.listdir("tic_tac_toe")
    # print(f"file path {directory}")
    board_state = read_board()

    # These user-instructions are provided and do not need to be changed.
    print("X goes first!")
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

    board_state = play_game(board_state)
    save_board(board_state)


if __name__ == "__main__":
    main()
