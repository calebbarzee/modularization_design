from pip import main
import json
import Board

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
        self.board = Board()

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
        board = self.board.curent_branch
        print("\t   A B C D E F G H I")
        print(f"""\t1 {board.A1} {board.B1} {board.C1}|{board.D1} {board.E1} {board.F1}|{board.G1} {board.H1} {board.I1}
\t1 {board.A2} {board.B2} {board.C2}|{board.D2} {board.E2} {board.F2}|{board.G2} {board.H2} {board.I2}
\t1 {board.A3} {board.B3} {board.C3}|{board.D3} {board.E3} {board.F3}|{board.G3} {board.H3} {board.I3}
\t1 {board.A4} {board.B4} {board.C4}|{board.D4} {board.E4} {board.F4}|{board.G4} {board.H4} {board.I4}
\t1 {board.A5} {board.B5} {board.C5}|{board.D5} {board.E5} {board.F5}|{board.G5} {board.H5} {board.I5}
\t1 {board.A6} {board.B6} {board.C6}|{board.D6} {board.E6} {board.F6}|{board.G6} {board.H6} {board.I6}
\t1 {board.A7} {board.B7} {board.C7}|{board.D7} {board.E7} {board.F7}|{board.G7} {board.H7} {board.I7}
\t1 {board.A8} {board.B8} {board.C8}|{board.D8} {board.E8} {board.F8}|{board.G8} {board.H8} {board.I8}
\t1 {board.A9} {board.B9} {board.C9}|{board.D9} {board.E9} {board.F9}|{board.G9} {board.H9} {board.I9}
""")

    def save_board(self, filename):
        with open("filename", "w") as board_file:
            board_file.write(json.dumps(self.board))

    def load_board(self, filename):
        with open(filename, "r") as board_file:
            json_string = board_file.read()
            self.board = json.loads(json_string)

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
        self.load_board(filename)


def main():
    pass


if __name__ == "__main__":
    main()
