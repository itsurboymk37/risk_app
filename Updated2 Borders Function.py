import numpy as np
from termcolor import colored

board = np.zeros((8, 8), dtype = int)

def borders(my_ter):
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

 

    

my_ter = [0.0, 0.6, 1.0, 1.1]
borders(my_ter)


