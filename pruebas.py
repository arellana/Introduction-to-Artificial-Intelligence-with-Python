"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Busco ganadores vertical y horizontal de X
    win = []

    #Recorre en filas y compara X
    for i in range(len(board[:][0])):
#        print('iteracion: ', i)
#        print('1:',board[i][0],'2:',board[i][1],'3:',board[i][2])
#        print((board[i][0] == X and board[i][1] == X and board[i][2] == X))
        if (board[i][0] == X and board[i][1] == X and board[i][2] == X):
#            print('Xfilas')
            win.append(X)

    #Recorre en columnas y compara X
    for j in range(len(board[0][:])):
#        print('iteracion: ', j)
#        print('1:',board[0][j],'2:',board[1][j],'3:',board[2][j])
        if (board[0][j] == X and board[1][j] == X and board[2][j] == X):
            win.append(X)
#            print('Xcol')

    #Recorro filas y compara O
    for ii in range(len(board[:][0])):
        if (board[ii][0] == O and board[ii][1] == O and board[ii][2] == O):
            win.append(O)

    #Recorre en columnas y compara O
    for jj in range(len(board[0][:])):
        if (board[0][jj] == O and board[1][jj] == O and board[2][jj] == O):
            win.append(O)


    #Veo diagonales
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X):
        win.append(X)
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O):
        win.append(O)
    elif (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        win.append(X)
    elif (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        win.append(O)


    ganador = None
    if len(win) != 0:
        for w in range(len(win)): 
            if win[w] == X:
                ganador = X
            elif win[w] == O:
                ganador = O
    print(win)

    return ganador  
    raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    vacios = boardPrue[0][:].count(EMPTY) + boardPrue[1][:].count(EMPTY) + boardPrue[2][:].count(EMPTY)
    
    if vacios == 0:
        return True
    else:
        return False


boardPrue = [[X, O, X],
            [X, 'c', O],
            [O, 'b', X]]

#print(boardPrue[1][:])
#print(boardPrue[1][:].count(X) + boardPrue[2][:].count(X) + boardPrue[0][:].count(X))

print(terminal(boardPrue))