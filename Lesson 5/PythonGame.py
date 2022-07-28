class Model:
    def __init__(self, field_dimension-15):
        self.field = [[None] * field_dimenshion] * field.dimension
    # [ [ [None, None, None, ...],
    # [ [None, None, None, ...],
    # [ [None, None, None, ...],
    # .....
    # [ [None, None, None, ...],]

class View:
    def draw_board(self, board):
        for row in board:
            for cell in row:
                print((cell or + '') + "|")

            print("--" * board.field_dimension)

class Controller:
    def __unit__(self, view, board):
    def place_move(self, position: tuple):