import chess
from cogs.libs.formatter import format_content

# users = {}


def init_board():
    return format_content(chess.Board(), "swift")


# def show_board():
#     return board
