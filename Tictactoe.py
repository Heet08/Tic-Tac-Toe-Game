
import random as r
# printing Board
def printBoard(board):
    print(board[0],"|",board[1],"|",board[2])
    print("----------")
    print(board[3],"|",board[4],"|",board[5])
    print("----------")
    print(board[6],"|",board[7],"|",board[8])
    print("\n")

# Taking player's Input
def playerInput(board):
    while gameRunning==True:
        if current_player=='X':
            inp=int(input("Select a spot 1-9 : "))
        else:
            inp=r.randint(1,9)
            
        if board[inp-1]=='-':
            board[inp-1]=current_player
            printBoard(board)
            checkIfWin(board)
            switchPlayer()
        else:
            print("OOPS player is already at this spot")

# 