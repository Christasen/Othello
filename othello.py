# Created by Guangyu Yan
# Modified by Thomas Shen
# All rights reserved.


import turtle
import math
import random
import numpy
import copy
from utility import nextn, getvalidMoves, isValidMove, oppon, count
from Minimax import MinimaxDecision

#draw green square
def square(length):
    turtle.speed(0) #speed everything up
    turtle.hideturtle() #hide our little turtle
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize(5)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.end_fill()
    turtle.pendown()

def circle(p1):
    turtle.speed(0) #speed everything up
    turtle.hideturtle() #hide our little turtle

    if p1 == 1:
        turtle.fillcolor('white')
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(45)
        turtle.end_fill()
        turtle.penup()
    elif p1 == -1:
        turtle.fillcolor('black')
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(45)
        turtle.end_fill()
        turtle.penup()

#Set the background
def drawcoordinate(board):
    turtle.speed(0) #speed everything up
    turtle.hideturtle() #hide our little turtle
    turtle.setworldcoordinates(0,0,1000,1000)
    FONT = ("Times",22)
    ###a way to speed everything up

    s = turtle.getscreen()
    s.tracer(0,0)

    for i in range(0,8):
        for j in range(0,8):
            turtle.penup()
            turtle.goto(100+i*100,100+j*100)
            turtle.pendown()
            square(100)
            #turtle.speed(0)
    for i in range(0,8):
        #turtle.speed(0)
        turtle.penup()
        turtle.goto(150+100*i,900)
        turtle.pendown()
        turtle.pencolor('black')
        turtle.write(i,font = FONT)
    for i in range(0,8):
        #turtle.speed(0)
        turtle.penup()
        turtle.goto(50,150+100*i)
        turtle.pendown()
        turtle.pencolor('black')
        turtle.write(7-i,font = FONT)
    for i in range(0,8):
        for j in range(0,8):
            #turtle.speed(0)
            turtle.penup()
            turtle.goto(150+j*100,800-i*100)
            turtle.pendown()
            circle(board[i][j])

#function part
###move function and draw a circle
def move(row,col,board):
    #turtle.speed(0)
    xco = 150 + col*100
    yco = 800 - row*100
    turtle.penup()
    turtle.goto(xco,yco)
    turtle.pendown()
    circle(board[row][col])

#define the flip function
def flip(row,col,board,color):
    turtle.speed(0)
    oppon3 = []
    oppon3,valid = oppon(row,col,board,color)
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
                move(r,c,board)
                r -= u
                c -= v

###computer part
### selectNewplay computer's funtion
def selectNextPlay(board):
    alist = getvalidMoves(board,1)
    result = MinimaxDecision(copy.deepcopy(board), alist, 1)
    if result == None: return
    [x, y] = result
    board[x][y] = 1
    move(x,y,board)
    flip(x,y,board,1)

###decision function
def desicion(white,black):
    w = str(white)
    b = str(black)

    if white > black:
        ts = turtle.textinput("End of the game", "Your Score: " + b + "\nComputer Score: " + w + "\nYou lose the game!") ##Sorry, Computer win the game.
        turtle.bye()
    elif white == black:
        ts = turtle.textinput("End of the game", "Your Score: " + b + "\nComputer Score: " + w + "\nIt's a draw!") #It is a draw in this case
        turtle.bye()
    else:
        ts = turtle.textinput("End of the game", "Your Score: " + b + "\nComputer Score: " + w + "\nYou win the game!") #Congratulations! You win the game!
        turtle.bye()
#check whether the board is full
def checkfull(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                count += 1
    return count


def judge1(string1,board):
    a = True
    #case1 quite the program if you enter a null string
    if string1 == '':
        white, black = count(board)
        desicion(white,black)
        #quit the turtle graph
        a = False
    return a

def judge2(board):
    a = True
    counta = checkfull(board)
    if counta == 0:
        white, black = count(board)
        desicion(white,black)
        #quit the turtle graph
        a = False
    return a

def main():
    turtle.speed(0) #speed everything up
    turtle.hideturtle() #hide our little turtle
    turtle.setworldcoordinates(0,0,1000,1000)
    FONT = ("Times",22)


    #initiallize the board of size8
    board1 = [0]*8
    for i in range(8):
        board1[i] = [0]*8
    board1[3][3] = 1  #1 #represents the white points
    board1[3][4] = -1 #-1 # represents the black points
    board1[4][3] = -1
    board1[4][4] = 1
    drawcoordinate(board1)
    togo = True
    while togo == True:

        alist = getvalidMoves(board1,-1)
        #case that the user did not have any valid move
        if alist == []:
            white, black = count(board1)
            desicion(white,black)
            #quit the turtle graph
            togo = False
        else:
            string1 = turtle.textinput("Othello Games","Enter row, col")
            #case1 quite the program if you enter a null string
            togo = judge1(string1,board1)
            if togo == True:
                togo = judge2(board1)

                if togo == True:
                    row = int(string1[0])
                    col = int(string1[2])
                    a = isValidMove(row,col,board1,-1)
                    while a == False:
                        str2 = str(row) + "," + str(col) + " is not a valid move. Reenter row,colomn"
                        string2 = turtle.textinput("Othello Games", str2)
                        togo2 = judge1(string2,board1)
                        if togo2 == True:
                            togo2 = judge2(board1)
                            if togo2 == True:
                                row = int(string2[0])
                                col = int(string2[2])
                                a = isValidMove(row,col,board1,-1)

                    board1[row][col] = -1
                    move(row,col,board1)
                    flip(row,col,board1,-1)
                    blist = getvalidMoves(board1,1)
                    if blist == []:
                        white, black = count(board1)
                        desicion(white,black)
                        #quit the turtle graph
                        togo = False
                    else:
                        selectNextPlay(board1)


if __name__ == "__main__":
    main()
