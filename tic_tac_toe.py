 #making the board

from turtle import position


board = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

playing_game = True
winner = None
current_player = "X"

#display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])          
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print(board[6] + " | " + board[7] + " | " + board[8])

display_board()

#main game 
def play_game():

    display_board()

    while playing_game:
        your_turn(current_player)
        check_game_over()
        change_player()
    
    if winner =="X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
def your_turn(player):


    print(player + "'s turn.")
    spot = input("pick a number from 1 to 9: ")

    valid = False
    while not valid:

        while spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            spot = input("pick a number from 1 to 9: ")
        spot = int(spot) - 1 

        if board[spot] == "-":
            valid = True
            
        else:
            print("spot already taken, pick a diferent number")
        board[spot] = player  
        display_board()

def check_game_over():
    check_win()
    check_tie()

def check_win():

    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global playing_game
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        playing_game = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global playing_game
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        playing_game = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global playing_game
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    
    if diagonals_1 or diagonals_2:
        playing_game = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    
    return

def check_tie():
    global playing_game
    if "-" not in board:
        playing_game = False
    return 

def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
   
play_game() 

