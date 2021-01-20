import chess

from cogs.libs.formatter import format_content

from cogs.libs.boards import boards


def legal_moves(_user_id):
    _board = boards[_user_id]
    return format_content(_board.legal_moves)


def legal_move(_user_id, _move):
    _board = boards[_user_id]
    return chess.Move.from_uci(_move) in _board.legal_moves
