import Branch


class Board():

    def __init__(self, board_state):
        self.board = board_state
        self.current_branch

    def remove_branch(self):
        pass

    def add_branch(self, pivot_point):
        new_branch = Branch(self.board, pivot_point)
        self.current_branch = new_branch
