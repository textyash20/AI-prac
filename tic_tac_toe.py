import os
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
win=1
Draw=-1
Running=0
stop=0
Game=Running
Mark='x'
def drawboard():
    print('%c|%c|%c'%(board[1],board[2],board[3]))
    print('__|__|__')
    print('%c|%c|%c'%(board[4],board[5],board[6]))
    print('__|__|__')
    print('%c|%c|%c'%(board[7],board[8],board[9]))
    print('|  |')
def check_for_winner():
    if(Game==Draw):
        print("Game Draw")
    if(Game==win):
        if(player==1):
            print("Player 1 won.")
        else:
            print("Player 2 won.")
def CheckPosition(x):
    try:
        if board[x] is ' ':
            return True
        else:
            print("The place is already occupied.")

            return False
    except IndexError:
        print("\n Please Enter")
def Check():
    global Game
    if(board[1]==board[2] and board[2]==board[3] and board[1]!=' '):
        Game=win
    elif(board[4]==board[5] and board[5]==board[6] and board[4]!=' '):
        Game=win
    elif(board[7]==board[8] and board[8]==board[9] and board[7]!=' '):
        Game=win
    elif(board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
        Game=win
    elif(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
        Game=win
    elif(board[3]==board[6] and board[6]==board[9] and board[3]!=' '):
        Game=win
    elif(board[1]==board[5] and board[5]==board[9] and board[5]!=' '):
        Game=win
    elif(board[3]==board[5] and board[5]==board[7] and board[5]!=' '):
        Game=win
    elif[1 for i in range(1,10) if board[i]!=' '].count(1)==9:
        Game=Draw
    else:
        Game=Running
def run_game():
    global player
    print('Tic-Tac-Toe  Game')
    print("Player 1[X]-----Player 2[O]")
    while Game is Running:
        drawboard()
        if player==1:
            print("Player 1's chance")
            Mark='X'
        else:
            print("Player 2's chance")
            Mark='O'
        choice=int(input('\n Enter the position between[1-9] where you want to mark:'))
        if(CheckPosition(choice)):
            board[choice]=Mark;
            Check()
        check_for_winner()
        if player==1:
            player=2
        else:
            player=1
run_game()
drawboard()
