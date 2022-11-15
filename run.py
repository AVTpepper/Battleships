# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint

print("Welcome to the game of Battleships!")


print("We want you to create a custom Battleship board.15")
print("Normally a Battleship board consists of 10 rows and 10 columns.")
print("This time, you get to decide the size of the battlefield.")
print("After every input you type into the game, press enter to continue.")


board_size = int(input("enter board size: ")) 


board = []

for x in range(board_size):
    board.append(["-"] * board_size)

print(board)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def print_board(board):
    """
    creates the board
    """
    letters = alphabet[0: (board_size)]
    print(letters)
    print("  %s%s" % (" "," ".join(letters)))
    row_number = 1
    for row in board:
        if row_number <= 9:
            print(" %d|%s|" % (row_number, "|".join(row)))
        else:
            print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1    
        


def making_ships():
    ship_placement = []
    ships_placed = 0
    ships_sunk = 0
    if board_size < 6:
        total_ships = 1
        print(f"There is {total_ships} ship in range commander, go shoot them down!")
        while ships_placed != total_ships:
            ship_row = randint(1, (board_size))
            ship_col = randint(1, (board_size))
            ship_location = [ship_row, ship_col]
            ship_placement.append(ship_location)
            ships_placed += 1
    elif board_size <= 10:
        total_ships = 3
        print(f"There are {total_ships} ships in range commander, go shoot them down!")
        while ships_placed != total_ships:
            ship_row = randint(1, (board_size))
            ship_col = randint(1, (board_size))
            ship_location = [ship_row, ship_col]
            ship_placement.append(ship_location)
            ships_placed += 1
    print(ship_placement)
    for turn in range(9):  

    # I want this to be in a second function, 
    # but Im stuck at how I can do that because of the variables 
    # I am using I have tried passing them through return___ and having them in paranthesis behind the def function(__)

        print(f"Turn {turn}")
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        guess = [guess_row, guess_col]
        if guess in ship_placement:
            print("Commander! You sunk a battleship!")
            board[guess_row - 1][guess_col - 1] = "O"
            ships_sunk += 1
        elif (guess_row < 1 or guess_row > board_size):
            print("Commander, your coordinates are out of range!")
            print(f"Try shooting within rows 1-{board_size} and columns 1-{board_size}")
        elif (board[guess_row - 1][guess_col - 1]) == "X" or (board[guess_row - 1][guess_col - 1]) == "O":
            print("Commander...You guessed that one already...")
        else:
            print("Commander, you missed the battleship, let's try again!")
            board[guess_row - 1][guess_col - 1] = "X"
        if turn == 8:
            print("Game Over")
        if ships_sunk == total_ships:
            print_board(board)
            print("Congratulations Commander, you have sunk all the ships!")
            print("Victory is ours, set sails, and let's go home!")
            break  
        turn += 1
        print_board(board)



print("Let's play Battleship!")
print_board(board)
making_ships()

