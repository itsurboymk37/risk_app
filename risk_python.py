
import sys
from termcolor import colored
import numpy as np

## Maybe I need to use a class with a bunch of different attributes. I don't think so tho: I think I just need a list (my_ter) to be filled with all the territories. 

## Creates board

board = np.zeros((8, 8), dtype = int)


## Prints board without colors

def print_board():
    for row in board:
        print (row)

## For joining imbedded lists

def jn(lis):
    im = []
    for i in lis:
        im.append(".".join(i))
    lis = im
    return lis

# For coloring the board appropriately

def color_board(my_ter):
    for j in my_ter:
        my_ter[my_ter.index(j)] = str(j).split(".")

    row = 0 #y
    col = 0 #x
    
    while row < len(board):
        
        while col < len(board[0]):
            
            h = [str(col), str(row)]
            hup = [str(col), str(row-1)]
            hdown = [str(col), str(row+1)]
            hright = [str(col+1), str(row)]
            hleft = [str(col-1), str(row)]
            # if I want to do it taking up less space, I could probs write it without the variables. But bcuz I don't care abt that rn, the variables make it more readable so imma keep them
            
            if h in my_ter:
                print (colored(board[row][col], "green"), end=" ")
                col += 1
                
            elif hup in my_ter or hdown in my_ter or hright in my_ter or hleft in my_ter:
                print (colored(board[row][col], "magenta"), end = " ")
                col += 1
                
            else:
                print (board[row][col], end=" ")
                col += 1

            if col != len(board[0]):
                print ("—", end = " ")
                
        print ("")
        row += 1
        col = 0
        if row != len(board):
            for i in range (len(board[0])):
                print ("|", end = "   ")
        print ("")



#Next I need to make it so that two people can play together (eg. having two lists you can enter to color the board
