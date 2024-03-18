
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
            print("OOPS spot is  already filled")

# Check for win and tie 
def checkWinner(board):
    global winner
    
    # horizontal
    for i in range(0,8,3):
        if board[i]==board[i+1]==board[i+2] and board[i]!='-':
            winner=board[i]
            return True
    
    # vertical
    for i in range(3):
        if board[i]==board[i+3]==board[i+6] and board[i]!='-':
            winner=board[i]
            return True
            
    # diagonal 
    if board[0]==board[4]==board[8] and board[0]!='-':
        winner=board[i]
        return True
    elif board[2]==board[4]==board[6] and board[2]!='-':
        winner=board[i]
        return True
    else:
        return False

def checkIfWin(board):
    global gameRunning
    if checkWinner(board):
        printBoard(board)
        print(f"Winner is {winner} !!")
        gameRunning=False
    else:
        tie=checkIfTie(board)
        if tie:
            gameRunning=False
        
def checkIfTie(board):
    if "-" not in board:
        print("Game tied !!")
        return True
    else:
        return False

# Switch Player
def switchPlayer():
    global current_player
    if current_player=="X":
        current_player="0"
    else:
        current_player="X"
        
printBoard(board)
playerInput(board)