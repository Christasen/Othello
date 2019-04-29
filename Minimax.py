import numpy
import math

def oppon(row, col, board, color):
    oppon1 = []
    for u in [-1,0,1]:
        for v in [-1,0,1]:
            if row + u >= 0 and col + v >= 0 and row + u < len(board) and col + v < len(board)\
            and board[row+u][col+v] == -color:
                oppon1.append([u,v])
    return oppon1

def flip(move, board, color):
    [row, col] = move
    oppon3 = []
    oppon3 = oppon(row,col,board,color)
    for el in oppon3:
        u = el[0]
        v = el[1]
        r = row + u
        c = col + v
        flip1 = [] ###@@@@
        while r >= 0 and c >= 0 and r < len(board) and c < len(board) and board[r][c] == -color:
            r += u
            c += v
            if r >= 0 and c >= 0 and r < len(board) and c < len(board):
                if board[r][c] == color:
                    flip1.append([r,c])
        if flip1 != []:
            r -= u
            c -= v
            while r != row or c!= col:
                board[r][c] = color
                r -= u
                c -= v
    return board

## Given a state(current board) in a game, calculate the best move by searching
## forward all the way to the terminal states.
def MinimaxDecision(board, valid_moves, player = 1):

    argmax = max
    infinity = math.inf

    def MaxValue(board, the_move, opponent, depth):
        # Final state check
        if len(valid_moves) == 0 or depth == 5:
            (black, white) = count(board)
            return (white - black)
        # Current player move
        v = -infinity
        new_board = flip(the_move, board, opponent)
        # Next movement from opponent
        next_valid_moves = getvalidMoves(new_board, -opponent)
        for next in next_valid_moves :
            v = max(v, MinValue(new_board, next, -opponent, depth + 1))
        return v

    def MinValue(board, the_move, opponent, depth):
        # Final state check
        if len(valid_moves) == 0 or depth == 5:
            (black, white) = count(board)
            return (white - black)
        # Current player move
        v = infinity
        new_board = flip(the_move, board, opponent)
        # Next movement from opponent
        next_valid_moves = getvalidMoves(new_board, -opponent)
        for next in next_valid_moves :
            v = min(v, MaxValue(new_board, next, -opponent, depth + 1))
        return v

    # Body of minimax_decision:
    best_score = -infinity
    best_choice = None
    for next in valid_moves:
        score = MinValue(board, next, player, 1)
        if best_score < score:
            best_score = score
            best_choice = next
    return best_choice
