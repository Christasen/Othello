import numpy

argmax = max

## Given a state(current board) in a game, calculate the best move by searching
## forward all the way to the terminal states.
def MinimaxDecision(board, valid_moves):

    def MaxValue(board, the_move):
        if len(valid_moves) == 0 :
            (black, white) = count(board)
            if black > white :
                return 1
            elif black < white :
                return -1
            else :
                return 0
        v = -infinity
        [x, y] = the_move
        move(x, y, board)
        flip(x, y, board, 1)
        next_valid_moves = getvalidMoves(board, 1)
        for [x, y] in new_valid_moves :
            v = max(v, MinValue(board, [x, y]))
        return v

    def MinValue(board, the_move):
        if len(valid_moves) == 0 :
            (black, white) = count(board)
            if black > white :
                return 1
            elif black < white :
                return -1
            else :
                return 0
        v = infinity
        [x, y] = the_move
        move(x, y, board)
        flip(x, y, board, 1)
        new_valid_moves = getvalidMoves(board, 1)
        for [x, y] in new_valid_moves :
            v = min(v, MaxValue(board, [x, y]))
        return v

    # Body of minimax_decision:
    return argmax(valid_moves, key=lambda a: MinValue(board, a))
