#I should imbedd borders in color_board

import sys
import os
from termcolor import colored
import numpy as np

###create board
board = np.zeros((4, 4), dtype = int)

def color_board(x, y):
    row = 0 #y
    col = 0 #x
    while row < len(board):
        while col < len(board[0]):
            if row == y and col == x:
                print (colored(board[y][x], "red"), end=" ")
                col += 1
            else:
                print (board[row][col], end=" ")
                col += 1
        print ("")
        row += 1
        col = 0
        
## now I want to input a list of territories, and have it color each one

def color_board2(inp):
    my_ter = []
    for i in inp:
        my_ter.append(i)
    print (my_ter)
    for j in my_ter:
        print (str(j))
        my_ter[my_ter.index(j)] = str(j).split(".")
    print (my_ter)
    row = 0 #y
    col = 0 #x
    while row < len(board):
        while col < len(board[0]):
            for i in range(len(my_ter)):
                if str(row) == my_ter[i][1] and str(col) == my_ter[i][0]:
                    print (colored(board[i+1][i], "red"), end=" ")
                    col += 1
                else:
                    print (board[row][col], end=" ")
                    col += 1
        print ("")
        row += 1
        col = 0

test = [2.1, 1.2]
color_board2(test)
