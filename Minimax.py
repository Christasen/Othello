import numpy
import math

## Given a state(current board) in a game, calculate the best move by searching
## forward all the way to the terminal states.
def MinimaxDecision(board, valid_moves, player = 1):

    argmax = max
    infinity = math.inf

    def MaxValue(board, the_move, opponent):
        # Final state check
        if len(valid_moves) == 0 :
            (black, white) = count(board)
            return (white - black)
        # Current player move
        v = -infinity
        [x, y] = the_move
        new_board = board
        flip(x, y, new_board, opponent)
        # Next movement from opponent
        next_valid_moves = getvalidMoves(new_board, -opponent)
        for next in next_valid_moves :
            v = max(v, MinValue(new_board, next, -opponent))
        return v

    def MinValue(board, the_move, opponent):
        # Final state check
        if len(valid_moves) == 0 :
            (black, white) = count(board)
            return (white - black)
        # Current player move
        v = infinity
        [x, y] = the_move
        new_board = board
        flip(x, y, new_board, opponent)
        # Next movement from opponent
        next_valid_moves = getvalidMoves(new_board, -opponent)
        for next in next_valid_moves :
            v = min(v, MaxValue(new_board, next, -opponent))
        return v

    # Body of minimax_decision:
    max_value = -infinity
    best_choice = []
    for next in valid_moves:
        new_value = MinValue(board, next, player)
        if max_value < new_value:
            max_value = new_value
            best_choice = next
    return best_choice
