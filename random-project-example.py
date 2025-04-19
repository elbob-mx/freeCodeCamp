import numpy as np # type: ignore
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def hit():
    print ("direct hit")
    board[guess_col][guess_row] = "H"
    print_board(board)

def miss():
    print ("you missed, try again")
    board[guess_col][guess_row]
    print_board(board)

def out_of_range():
    print ("this is out of the range of the battle field")

def players_turn():
    for turn in range(4):
        print ("turn", turn +1)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        if guess_col == ship_col and guess_row == ship_row:
            hit()
        elif guess_col not in range(5) or guess_row not in range(5) :
            out_of_range()
        else:
            miss()

ship_row = random_row(board)
ship_col = random_col(board)

if_yes = str(input("Do you want to play Battleship? "))

if if_yes == 'yes':
    print (ship_row)
    print (ship_col)
    players_turn()