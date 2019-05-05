# Created by Guangyu Yan
# Modified by Thomas Shen
# All rights reserved.

def nextn(row,col,board,color,u,v):
    #row += u
    #col += v
    valid = False
    while row >= 0 and col >= 0  and row < len(board) and col < len(board):
        row += u
        col += v
        if row >= 0 and col >= 0 and row<len(board) and col < len(board):

            if board[row][col] == 0:
                break
            elif board[row][col] == color:
                valid = True
                break
    return valid

def getvalidMoves(board,color):
    newlist = []
    for i in range(8):
        for j in range(8):
            a = isValidMove(i,j,board,color)
            if a == True:
                newlist.append([i,j])
    return newlist

## isValidMove
def isValidMove(row,col,board,color):
    # if color == 'white':
    #     color = 1
    # elif color == 'black':
    #     color = -1
    oppon2 = 0
    if board[row][col] != 0:
        return False
    oppon2,valid = oppon(row,col,board,color)
    if valid == False:
        return False
    for el in oppon2:
        if nextn(row,col,board,color,el[0],el[1]) == True:
            return True
    return False

#helper function1
def oppon(row,col,board,color):
    oppon1 = []
    valid = False
    for u in [-1,0,1]:
        for v in [-1,0,1]:
            if row + u >= 0 and col + v >= 0 and row + u < len(board) and col + v < len(board)\
            and board[row+u][col+v] == -color:
                oppon1.append([u,v])
                valid = True
    return oppon1, valid

##calculate the numbers of 1s in the board
def count(board):
    white = 0
    black = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                white += 1
            elif board[i][j] == -1:
                black += 1
    return white, black
