from ast import match_case
import json

# 1. Name:
#      Caleb Barzee
# 2. Assignment Name:
#      Lab 06 : Sudoku Draft
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting


def get_filename():
    filename = input("Where is your board located? ")
    return filename


def get_action():
    action = input(
        "Please type your desired action ('"'g'"' to guess, '"'p'"' for possible values, and '"'s'"' to save)\nAction: ")
    return action


def get_coor():
    coor = input(
        "Please enter the desired coordinate (A1-I9): ").strip().upper()
    # make sure it's a valid coordinate
    match str(coor)[0]:
        case "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I": is_valid = True
        case _: is_valid = False

    match int(str(coor)[1]):
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9: is_valid = True
        case _: is_valid = False

    if not is_valid:
        print("Unacceptable value entered.")
        get_coor()

    match coor:
        case "A1": coor = (0, 0)
        case "A2": coor = (1, 0)
        case "A3": coor = (2, 0)
        case "A4": coor = (3, 0)
        case "A5": coor = (4, 0)
        case "A6": coor = (5, 0)
        case "A7": coor = (6, 0)
        case "A8": coor = (7, 0)
        case "A9": coor = (8, 0)
        case "B1": coor = (0, 1)
        case "B2": coor = (1, 1)
        case "B3": coor = (2, 1)
        case "B4": coor = (3, 1)
        case "B5": coor = (4, 1)
        case "B6": coor = (5, 1)
        case "B7": coor = (6, 1)
        case "B8": coor = (7, 1)
        case "B9": coor = (8, 1)
        case "C1": coor = (0, 2)
        case "C2": coor = (1, 2)
        case "C3": coor = (2, 2)
        case "C4": coor = (3, 2)
        case "C5": coor = (4, 2)
        case "C6": coor = (5, 2)
        case "C7": coor = (6, 2)
        case "C8": coor = (7, 2)
        case "C9": coor = (8, 2)
        case "D1": coor = (0, 3)
        case "D2": coor = (1, 3)
        case "D3": coor = (2, 3)
        case "D4": coor = (3, 3)
        case "D5": coor = (4, 3)
        case "D6": coor = (5, 3)
        case "D7": coor = (6, 3)
        case "D8": coor = (7, 3)
        case "D9": coor = (8, 3)
        case "E1": coor = (0, 4)
        case "E2": coor = (1, 4)
        case "E3": coor = (2, 4)
        case "E4": coor = (3, 4)
        case "E5": coor = (4, 4)
        case "E6": coor = (5, 4)
        case "E7": coor = (6, 4)
        case "E8": coor = (7, 4)
        case "E9": coor = (8, 4)
        case "F1": coor = (0, 5)
        case "F2": coor = (1, 5)
        case "F3": coor = (2, 5)
        case "F4": coor = (3, 5)
        case "F5": coor = (4, 5)
        case "F6": coor = (5, 5)
        case "F7": coor = (6, 5)
        case "F8": coor = (7, 5)
        case "F9": coor = (8, 5)
        case "G1": coor = (0, 6)
        case "G2": coor = (1, 6)
        case "G3": coor = (2, 6)
        case "G4": coor = (3, 6)
        case "G5": coor = (4, 6)
        case "G6": coor = (5, 6)
        case "G7": coor = (6, 6)
        case "G8": coor = (7, 6)
        case "G9": coor = (8, 6)
        case "H1": coor = (0, 7)
        case "H2": coor = (1, 7)
        case "H3": coor = (2, 7)
        case "H4": coor = (3, 7)
        case "H5": coor = (4, 7)
        case "H6": coor = (5, 7)
        case "H7": coor = (6, 7)
        case "H8": coor = (7, 7)
        case "H9": coor = (8, 7)
        case "I1": coor = (0, 8)
        case "I2": coor = (1, 8)
        case "I3": coor = (2, 8)
        case "I4": coor = (3, 8)
        case "I5": coor = (4, 8)
        case "I6": coor = (5, 8)
        case "I7": coor = (6, 8)
        case "I8": coor = (7, 8)
        case "I9": coor = (8, 8)

        case "1A": coor = (0, 0)
        case "2A": coor = (1, 0)
        case "3A": coor = (2, 0)
        case "4A": coor = (3, 0)
        case "5A": coor = (4, 0)
        case "6A": coor = (5, 0)
        case "7A": coor = (6, 0)
        case "8A": coor = (7, 0)
        case "9A": coor = (8, 0)
        case "1B": coor = (0, 1)
        case "2B": coor = (1, 1)
        case "3B": coor = (2, 1)
        case "4B": coor = (3, 1)
        case "5B": coor = (4, 1)
        case "6B": coor = (5, 1)
        case "7B": coor = (6, 1)
        case "8B": coor = (7, 1)
        case "9B": coor = (8, 1)
        case "1C": coor = (0, 2)
        case "2C": coor = (1, 2)
        case "3C": coor = (2, 2)
        case "4C": coor = (3, 2)
        case "5C": coor = (4, 2)
        case "6C": coor = (5, 2)
        case "7C": coor = (6, 2)
        case "8C": coor = (7, 2)
        case "9C": coor = (8, 2)
        case "1D": coor = (0, 3)
        case "2D": coor = (1, 3)
        case "3D": coor = (2, 3)
        case "4D": coor = (3, 3)
        case "5D": coor = (4, 3)
        case "6D": coor = (5, 3)
        case "7D": coor = (6, 3)
        case "8D": coor = (7, 3)
        case "9D": coor = (8, 3)
        case "1E": coor = (0, 4)
        case "2E": coor = (1, 4)
        case "3E": coor = (2, 4)
        case "4E": coor = (3, 4)
        case "5E": coor = (4, 4)
        case "6E": coor = (5, 4)
        case "7E": coor = (6, 4)
        case "8E": coor = (7, 4)
        case "9E": coor = (8, 4)
        case "1F": coor = (0, 5)
        case "2F": coor = (1, 5)
        case "3F": coor = (2, 5)
        case "4F": coor = (3, 5)
        case "5F": coor = (4, 5)
        case "6F": coor = (5, 5)
        case "7F": coor = (6, 5)
        case "8F": coor = (7, 5)
        case "9F": coor = (8, 5)
        case "1G": coor = (0, 6)
        case "2G": coor = (1, 6)
        case "3G": coor = (2, 6)
        case "4G": coor = (3, 6)
        case "5G": coor = (4, 6)
        case "6G": coor = (5, 6)
        case "7G": coor = (6, 6)
        case "8G": coor = (7, 6)
        case "9G": coor = (8, 6)
        case "1H": coor = (0, 7)
        case "2H": coor = (1, 7)
        case "3H": coor = (2, 7)
        case "4H": coor = (3, 7)
        case "5H": coor = (4, 7)
        case "6H": coor = (5, 7)
        case "7H": coor = (6, 7)
        case "8H": coor = (7, 7)
        case "9H": coor = (8, 7)
        case "1I": coor = (0, 8)
        case "2I": coor = (1, 8)
        case "3I": coor = (2, 8)
        case "4I": coor = (3, 8)
        case "5I": coor = (4, 8)
        case "6I": coor = (5, 8)
        case "7I": coor = (6, 8)
        case "8I": coor = (7, 8)
        case "9I": coor = (8, 8)

    return coor


def get_value():
    value = int(input(
        "Please enter the desired value (1-9): "))
    # make sure it's a valid value
    match value:
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9: is_valid = True
        case _: is_valid = False

    if not is_valid:
        print("Unacceptable value entered.")
        get_value()

    return value


def display_board(board):
    #       Example of a board displayed
    #              A B C D E F G H I
    #           1  7 2 3|     |1 5 9
    #           2  6    |3   2|    8
    #           3  8    |  1  |    2
    #              -----+-----+-----
    #           4    7  |6 5 4|  2
    #           5      4|2   7|3
    #           6    5  |9 3 1|  4
    #              -----+-----+-----
    #           7  5    |  7  |    3
    #           8  4    |1   3|    6
    #           9  9 3 2|     |7 1 4
    d_board = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        d_board[i].append(board[i][0])
        d_board[i].append(board[i][1])
        d_board[i].append(board[i][2])
        d_board[i].append(board[i][3])
        d_board[i].append(board[i][4])
        d_board[i].append(board[i][5])
        d_board[i].append(board[i][6])
        d_board[i].append(board[i][7])
        d_board[i].append(board[i][8])
    for i in range(9):
        for j in range(9):
            if d_board[i][j] == 0:
                d_board[i][j] = " "
    print("\t   A B C D E F G H I")
    for i in range(9):
        print(
            f"\t{i+1}  {d_board[i][0]} {d_board[i][1]} {d_board[i][2]}|{d_board[i][3]} {d_board[i][4]} {d_board[i][5]}|{d_board[i][6]} {d_board[i][7]} {d_board[i][8]}")
        if i == 2 or i == 5:
            print("\t -------+-----+-----")


def display_possible():
    pass


def save_board(board):
    with open("saved_board.json", "w") as board_file:
        board_file.write(json.dumps(board))


def load_board():
    with open("saved_board.json", "r") as board_file:
        json_string = board_file.read()
        board = json.loads(json_string)
        return board


def convert_array(filename):
    with open(filename, "r") as board_file:
        json_string = board_file.read()
        board_array = json.loads(json_string)
        board_state = {"current": 1, "board1": {
            "1": [[], [], [], [], [], [], [], [], []], "1p": []}}
    for i in range(0, 9):
        board_state["board1"]["1"][i].append(board_array["board"][i][0])
        board_state["board1"]["1"][i].append(board_array["board"][i][1])
        board_state["board1"]["1"][i].append(board_array["board"][i][2])
        board_state["board1"]["1"][i].append(board_array["board"][i][3])
        board_state["board1"]["1"][i].append(board_array["board"][i][4])
        board_state["board1"]["1"][i].append(board_array["board"][i][5])
        board_state["board1"]["1"][i].append(board_array["board"][i][6])
        board_state["board1"]["1"][i].append(board_array["board"][i][7])
        board_state["board1"]["1"][i].append(board_array["board"][i][8])
    return board_state
    # "pivot_coor": "", "pivot_value": ""
    # pivot_coor and pivot_value to be added when a new branch is initialized
    # this is the main branch and thus there is no pivot_point
    # current is also to be updated so the game know which branch to start with


def check_coor(coor, board):
    assert type(coor) == type((1, 1))
    if board[coor[0]][coor[1]] == 0:
        return True
    return False


def check_value(coor, value, board):
    assert type(value) == type(1)
    assert type(coor) == type((1, 1))
    # check row
    if value in board[coor[0]]:
        return False
    # check column
    for i in range(9):
        if board[i][coor[1]] == value:
            return False
    box = 1
    # check box
    match coor:
        case (0, 0) | (0, 1) | (0, 2) | (1, 0) | (1, 1) | (1, 2) | (2, 0) | (2, 1) | (2, 2): box = 1
        case (0, 3) | (0, 4) | (0, 5) | (1, 3) | (1, 4) | (1, 5) | (2, 3) | (2, 4) | (2, 5): box = 2
        case (0, 6) | (0, 7) | (0, 8) | (1, 6) | (1, 7) | (1, 8) | (2, 6) | (2, 7) | (2, 8): box = 3
        case (3, 0) | (3, 1) | (3, 2) | (4, 0) | (4, 1) | (4, 2) | (5, 0) | (5, 1) | (5, 2): box = 4
        case (3, 3) | (3, 4) | (3, 5) | (4, 3) | (4, 4) | (4, 5) | (5, 3) | (5, 4) | (5, 5): box = 5
        case (3, 6) | (3, 7) | (3, 8) | (4, 6) | (4, 7) | (4, 8) | (5, 6) | (5, 7) | (5, 8): box = 6
        case (6, 0) | (6, 1) | (6, 2) | (7, 0) | (7, 1) | (7, 2) | (8, 0) | (8, 1) | (8, 2): box = 7
        case (6, 3) | (6, 4) | (6, 5) | (7, 3) | (7, 4) | (7, 5) | (8, 3) | (8, 4) | (8, 5): box = 8
        case (6, 6) | (6, 7) | (6, 8) | (7, 6) | (7, 7) | (7, 8) | (8, 6) | (8, 7) | (8, 8): box = 9

    if box == 1:
        if value == board[0][0]:
            return False
        elif value == board[0][1]:
            return False
        elif value == board[0][2]:
            return False
        elif value == board[1][0]:
            return False
        elif value == board[1][1]:
            return False
        elif value == board[1][2]:
            return False
        elif value == board[2][0]:
            return False
        elif value == board[2][1]:
            return False
        elif value == board[2][2]:
            return False
    elif box == 2:
        if value == board[0][3]:
            return False
        elif value == board[0][4]:
            return False
        elif value == board[0][5]:
            return False
        elif value == board[1][3]:
            return False
        elif value == board[1][4]:
            return False
        elif value == board[1][5]:
            return False
        elif value == board[2][3]:
            return False
        elif value == board[2][4]:
            return False
        elif value == board[2][5]:
            return False
    elif box == 3:
        if value == board[0][6]:
            return False
        elif value == board[0][7]:
            return False
        elif value == board[0][8]:
            return False
        elif value == board[1][6]:
            return False
        elif value == board[1][7]:
            return False
        elif value == board[1][8]:
            return False
        elif value == board[2][6]:
            return False
        elif value == board[2][7]:
            return False
        elif value == board[2][8]:
            return False
    elif box == 4:
        if value == board[3][0]:
            return False
        elif value == board[3][1]:
            return False
        elif value == board[3][2]:
            return False
        elif value == board[4][0]:
            return False
        elif value == board[4][1]:
            return False
        elif value == board[4][2]:
            return False
        elif value == board[5][0]:
            return False
        elif value == board[5][1]:
            return False
        elif value == board[5][2]:
            return False
    elif box == 5:
        if value == board[3][3]:
            return False
        elif value == board[3][4]:
            return False
        elif value == board[3][5]:
            return False
        elif value == board[4][3]:
            return False
        elif value == board[4][4]:
            return False
        elif value == board[4][5]:
            return False
        elif value == board[5][3]:
            return False
        elif value == board[5][4]:
            return False
        elif value == board[5][5]:
            return False
    elif box == 6:
        if value == board[3][6]:
            return False
        elif value == board[3][7]:
            return False
        elif value == board[3][8]:
            return False
        elif value == board[4][6]:
            return False
        elif value == board[4][7]:
            return False
        elif value == board[4][8]:
            return False
        elif value == board[5][6]:
            return False
        elif value == board[5][7]:
            return False
        elif value == board[5][8]:
            return False
    elif box == 7:
        if value == board[6][0]:
            return False
        elif value == board[6][1]:
            return False
        elif value == board[6][2]:
            return False
        elif value == board[7][0]:
            return False
        elif value == board[7][1]:
            return False
        elif value == board[7][2]:
            return False
        elif value == board[8][0]:
            return False
        elif value == board[8][1]:
            return False
        elif value == board[8][2]:
            return False
    elif box == 8:
        if value == board[6][3]:
            return False
        elif value == board[6][4]:
            return False
        elif value == board[6][5]:
            return False
        elif value == board[7][3]:
            return False
        elif value == board[7][4]:
            return False
        elif value == board[7][5]:
            return False
        elif value == board[8][3]:
            return False
        elif value == board[8][4]:
            return False
        elif value == board[8][5]:
            return False
    elif box == 9:
        if value == board[6][6]:
            return False
        elif value == board[6][7]:
            return False
        elif value == board[6][8]:
            return False
        elif value == board[7][6]:
            return False
        elif value == board[7][7]:
            return False
        elif value == board[7][8]:
            return False
        elif value == board[8][6]:
            return False
        elif value == board[8][7]:
            return False
        elif value == board[8][8]:
            return False
    return True


def check_board(board):
    # Ensures that the board is in a playable state.
    # Checks for win condition of all values filled.
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return "unfilled"


def store_value(coor, value, board):
    assert type(value) == type(1)
    assert type(coor) == type((1, 1))
    board[coor[0]][coor[1]] = value
    return board


def update_possible():
    pass


def remove_branch():
    pass


def add_branch(board, coor, value):
    new_branch = board
    new_branch["current"] += 1


def solve_board():
    pass


def main():

    # Get the filename only if you wish to convert the original test array files.
    # Otherwise simply call sudoku.load_board and the last saved game will be
    # loaded, the saved games are always stored as ./saved.board.json

    # filename = get_filename()
    # board = convert_array(filename)
    board = load_board()
    current_board = board["board1"]["1"]
    while check_board(current_board) == "unfilled":
        display_board(current_board)
        action = get_action()
        if action == "p":
            display_possible()
        elif action == "s":
            save_board(board)
            print("Your game has been saved. Thank you for playing.")
            break
        coor = get_coor()
        while not check_coor(coor, current_board):
            print("This Coordinate is already filled. Please try another.")
            coor = get_coor()
        value = get_value()
        while not check_value(coor, value, current_board):
            print("This value is not valid in this location. Please try another.")
            value = get_value()
        current_board = store_value(coor, value, current_board)


if __name__ == "__main__":
    main()
