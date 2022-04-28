 #making the board

from turtle import position


board = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

#display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])          
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print(board[6] + " | " + board[7] + " | " + board[8])

display_board()

#main game 
def play_game():

    display_board()

    your_turn()

def your_turn():
    spot = input("pick a number from 1 to 9: ")
    spot = int(position) - 1 

play_game() 

