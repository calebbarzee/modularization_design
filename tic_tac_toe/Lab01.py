# 1. Name:
#      Caleb Barzee
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
import json
import constants


def initialize_blank_board():
    board_state = {
        "board": [
            constants.BLANK, constants.BLANK, constants.BLANK,
            constants.BLANK, constants.BLANK, constants.BLANK,
            constants.BLANK, constants.BLANK, constants.BLANK]
    }
    return board_state


def read_board():
    '''Read the previously existing board from the file if it exists.'''
    with open("tic_tac_toe/board.json") as board_file:
        board_state = json.loads(board_file.read())

    return board_state


def save_board(board):
    '''Save the current game to a file.'''
    with open("tic_tac_toe/board.json") as board_file:
        board_file.write(json.dumps(board_state['board']))


def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(
        f" {board_state['board'][0]} | {board_state['board'][1]} | {board_state['board'][2]} ")
    print("---+---+---")
    print(
        f" {board_state['board'][3]} | {board_state['board'][4]} | {board_state['board'][5]} ")
    print("---+---+---")
    print(
        f" {board_state['board'][6]} | {board_state['board'][7]} | {board_state['board'][8]} \n")


def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    return True


def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    print("The current board is:")
    display_board(board)
    response = input()
    if response == "q":
        return False

# Why would we ever desire to hide the results from the user?


def game_done(board, message=True):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != constants.BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != constants.BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != constants.BLANK and (board[0] == board[4] == board[8] or
                                        board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == constants.BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    return False


def main():
    # A blank Tic-Tac-Toe board. We should not need to change this board;
    # it is only used to reset the board to blank. This should be the format
    # of the code in the JSON file.
    board_state = read_board()

    # These user-instructions are provided and do not need to be changed.
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

    while not game_done(board_state["board"]):
        q_response = play_game(board_state["board"])
        if not q_response:
            save_board(board_state)
            return
