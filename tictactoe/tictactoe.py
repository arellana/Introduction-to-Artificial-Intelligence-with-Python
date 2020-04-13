"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #Conteo de casilleros ocupados 
    cantX = 0
    cantO = 0
    for i in range(len(board[:][0])):
        for j in range(len(board[0][:])):
            if board[i][j] == X:
                cantX += 1 
            elif board[i][j] == O:
                cantO += 1 
            else:
                pass

    #Veo de quien es el turno
    if cantX == 0 or cantX == cantO: #Si no movi nunca o 
        turn = X
    elif cantX != 0 and cantX > cantO:
        turn = O
    else:
        print('Algo anda mal en los turnos')

    return turn

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    #accion va a ser un conjunto de los lugares vacios en donde puedo poner X o O
    accion = set()

    #relleno en conjunto con los vacios
    for i in range(len(board[:][0])):
        for j in range(len(board[0][:])):
            if board[i][j] == EMPTY:
                accion.add((i,j)) 

    return accion
    
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    #Creo una copia del estado original y lo lleno de la accion que se realizo (poner una X o O)
    nuevoTab = copy.deepcopy(board)

    if action in actions(board):
        #board me va a enviar el lugar donde pulsaron, veo de quien es el turno y eso lo relleno en el nuevo lugar
        nuevoTab[action[0]][action[1]] = player(board)
    else:
        print('Casillero no disponible')

    #result = copy.deepcopy(board)
    #nuevoTab[action[0]][action[1]] = player(board)
    return nuevoTab

    raise NotImplementedError


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
    if len(win) == 1:
        for w in range(len(win)): 
            if win[w] == X:
                ganador = X
            elif win[w] == O:
                ganador = O
    elif len(win) > 1:
#        print('Error: Multiples ganadores')


    return ganador  
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    vacios = board[0][:].count(EMPTY) + board[1][:].count(EMPTY) + board[2][:].count(EMPTY)
    
    if vacios == 0:
        return True
    elif winner(board) != None:
        return True
    else:
        return False


    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif terminal(board) == True and winner(board) == None:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #Si no termino la partida, analizo el movimiento
    if terminal(board):
    	return None

    else: #Si le toca a X que piense
        if player(board) == X:
        	value, jugada = maxiScore(board)
        	return jugada
        elif player(board) == O:
        	value, jugada = miniScore(board)
        	return jugada

    raise NotImplementedError


def maxiScore(board):

    if terminal(board): #Si ya termino el juego, listo, devolve el score
        return utility(board), None	

    #Si no termino voy a extremar
    vfinal = float('-inf')
    movim = None

    #Miro las acciones permitidas
    for action in actions(board):

    	#Minimizo la accion de haber movido
        ext, vfinal = miniScore(result(board, action))
        if ext > vfinal:
            vfinal = ext
            movim = action
            if vfinal == 1: #Que es lo que quiero que suceda para maximizar score de X
                return vfinal, movim

    return vfinal, movim

def miniScore(board):

    if terminal(board): #Si ya termino el juego, listo, devolve el score
        return utility(board), None	

    #Si no termino voy a extremar
    vfinal = float('inf')
    movim = None

    #Miro las acciones permitidas
    for action in actions(board):

    	#Maximizo la accion de haber movido
        ext, act = maxiScore(result(board, action))

        if ext < vfinal:
            vfinal = ext
            movim = action
            if vfinal == -1: #Que es lo que quiero que suceda para minimizar score de O
                return vfinal, movim

    return vfinal, movim
