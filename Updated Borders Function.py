import sys
from termcolor import colored
import numpy as np

## Creates board

board = np.zeros((8, 8), dtype = int)

## New borders function 

def borders(my_ter):
    for j in my_ter:
        my_ter[my_ter.index(j)] = str(j).split(".")
    print (my_ter)
    ##I should use the same loops as the territories function: I can test if something is directly to the right, left, up, or down and then if it is print it correctly.
    ##I can also check if it is in my_ter already (in which case, no need to print it in borders)
    ##Also, I am going to want to put territories and borders together (so I only print the board once)
    ###Maybe it is as simple as adding an elif statement to the territories function
    row = 0 #y
    col = 0 #x
    h = [str(col), str(row)]
    if h in my_ter:
        print (h)
    k = 0
    while row < len(board):
        while col < len(board[0]):
            for i in range(len(my_ter)):
                if str(row) == my_ter[i][1] and str(col) == my_ter[i][0]:
                    print (colored(board[row][col], "green"), end=" ")
                    col += 1
                    break
                ## need something to check if row/col is not in list at all. bcuz if it is the third item in the list but borders the first item, it will print a border not a territory. 
                elif row == int(my_ter[i][1]) and col == int(my_ter[i][0]) + 1:
                    print (colored(board[row][col], "magenta"), end = " ")
                    col += 1
                    break
                elif row == int(my_ter[i][1]) and col == int(my_ter[i][0]) - 1 and h not in my_ter:
                    print (colored(board[row][col], "magenta"), end = " ")
                    col += 1
                    break
                elif row == int(my_ter[i][1]) + 1 and col == int(my_ter[i][0]) and h not in my_ter:
                    print (colored(board[row][col], "magenta"), end = " ")
                    col += 1
                    break
                elif row == int(my_ter[i][1]) - 1 and col == int(my_ter[i][0]) and h not in my_ter:
                    print (colored(board[row][col], "magenta"), end = " ")
                    col += 1
                    break
                else:
                    k = i
                    if k == len(my_ter)-1:   
                        print (board[row][col], end=" ")
                        k = 0
                        col += 1
        print ("")
        row += 1
        col = 0

 

    

my_ter = [0.0, 0.1, 1.0, 1.1]
borders(my_ter)

