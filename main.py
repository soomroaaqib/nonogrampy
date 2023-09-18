from constants import BoardSize
from board import prepare_board


if __name__ == "__main__":
    board_size = int(input("Board Size: "))
    if board_size not in BoardSize.values():
        raise Exception("Incorrect board size!")

    board = prepare_board(board_size)

