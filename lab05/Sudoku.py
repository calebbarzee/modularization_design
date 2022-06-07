from pip import main
import json
import Branch

# 1. Name:
#      Caleb Barzee
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting


class Sudoku():
    def __init__(self):
        self.board = {}

    def prompt_filename(self):
        filename = input("Where is your board located? ")
        return filename

    def prompt_coor(self):
        coor = input("Please enter the desired coordinate: ").upper
        # make sure it's a valid coordinate

        self.check_coor(coor)

    def prompt_value(self):
        value = int(input("Please enter the desired value: "))
        # make sure it's a valid value

        self.check_value(value)

    def display_board(self):
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
        board = self.board["board"]["1"]
        print("\t  A B C D E F G H I")
        print(f"""\t1 {board["A1"]} {board["B1"]} {board["C1"]}|{board["D1"]} {board["E1"]} {board["F1"]}|{board["G1"]} {board["H1"]} {board["I1"]}
\t2 {board["A2"]} {board["B2"]} {board["C2"]}|{board["D2"]} {board["E2"]} {board["F2"]}|{board["G2"]} {board["H2"]} {board["I2"]}
\t3 {board["A3"]} {board["B3"]} {board["C3"]}|{board["D3"]} {board["E3"]} {board["F3"]}|{board["G3"]} {board["H3"]} {board["I3"]}
\t-------+-----+-----
\t4 {board["A4"]} {board["B4"]} {board["C4"]}|{board["D4"]} {board["E4"]} {board["F4"]}|{board["G4"]} {board["H4"]} {board["I4"]}
\t5 {board["A5"]} {board["B5"]} {board["C5"]}|{board["D5"]} {board["E5"]} {board["F5"]}|{board["G5"]} {board["H5"]} {board["I5"]}
\t6 {board["A6"]} {board["B6"]} {board["C6"]}|{board["D6"]} {board["E6"]} {board["F6"]}|{board["G6"]} {board["H6"]} {board["I6"]}
\t-------+-----+-----
\t7 {board["A7"]} {board["B7"]} {board["C7"]}|{board["D7"]} {board["E7"]} {board["F7"]}|{board["G7"]} {board["H7"]} {board["I7"]}
\t8 {board["A8"]} {board["B8"]} {board["C8"]}|{board["D8"]} {board["E8"]} {board["F8"]}|{board["G8"]} {board["H8"]} {board["I8"]}
\t9 {board["A9"]} {board["B9"]} {board["C9"]}|{board["D9"]} {board["E9"]} {board["F9"]}|{board["G9"]} {board["H9"]} {board["I9"]}
""")

    def save_board(self):
        with open("saved_board.json", "w") as board_file:
            board_file.write(json.dumps(self.board))

    def load_board(self):
        with open("saved_board.json", "r") as board_file:
            json_string = board_file.read()
            self.board = json.loads(json_string)

    def convert_array(self, filename):
        with open(filename, "r") as board_file:
            json_string = board_file.read()
            board_array = json.loads(json_string)
            board_state = {"board": {"1": {}, "1p": {}, "pivot_point": 0}}
        for i in range(len(board_array["board"])):
            board_state["board"]["1"][f"A{i + 1}"] = board_array["board"][i][0]
            board_state["board"]["1"][f"B{i + 1}"] = board_array["board"][i][1]
            board_state["board"]["1"][f"C{i + 1}"] = board_array["board"][i][2]
            board_state["board"]["1"][f"D{i + 1}"] = board_array["board"][i][3]
            board_state["board"]["1"][f"E{i + 1}"] = board_array["board"][i][4]
            board_state["board"]["1"][f"F{i + 1}"] = board_array["board"][i][5]
            board_state["board"]["1"][f"G{i + 1}"] = board_array["board"][i][6]
            board_state["board"]["1"][f"H{i + 1}"] = board_array["board"][i][7]
            board_state["board"]["1"][f"I{i + 1}"] = board_array["board"][i][8]
        # Everytime a new board is parsed in then the pivot_point is 0
        # because this is the main branch and thus there is no pivot_point
        self.board = board_state

    def check_board(self):
        pass

    def check_coor(self, coor):
        pass

    def check_value(self, value):
        assert type(value) == type(1)

    def update_possible(self):
        pass

    def solve_board(self):
        pass

    def play_game(self):
        filename = self.prompt_filename()
        self.load_board()


def main():
    # Initialize a new instance of the game
    sudoku = Sudoku()
    # Get the filename only if you wish to convert the original test array files.
    # Otherwise simply call sudoku.load_board and the last saved game will be
    # loaded, the saved games are always stored as ./saved.board.json
    filename = sudoku.prompt_filename()
    sudoku.convert_array(filename)
    sudoku.display_board()
    sudoku.save_board()


if __name__ == "__main__":
    main()
