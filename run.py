"""
This file includes the battleship code.
Information for the player:
- Can has a maximum size of 10 rows and 10 columns.
- The board will always have the same amount of rows and columns.
- The size you chose will multiply by itself.
    - Example: a board size 3 would be 3 rows and 3 columns.
- Columns are represented by letters.
- Rows are represented by numbers.
- You will always guess row first, then followed by columns.
- The ships will be hidden on the board.
- If you hit a ship it will be marked with an "O".
- If you miss a ship it will be marked with an "X"
"""
from random import randint
import os
import sys


os.system('clear')
print("               Welcome to the game of Battleships!")
print("--------------------------------------------------------------------")
print("         We want you to create a custom Battleship board.")
print("   Normally a Battleship board consists of 10 rows and 10 columns.")
print("      This time, you get to decide the size of the battlefield.")
print("  After every input you type into the game, press enter to continue.")
print("--------------------------------------------------------------------")
while True:
    BOARD_SIZE = input(" Enter board size: ")
    if BOARD_SIZE.isdigit():
        BOARD_SIZE = int(BOARD_SIZE)
        if BOARD_SIZE > 1 and BOARD_SIZE <= 10:
            print(" ")
            print("Perfect, let's sail out and find the enemies Commander!")
            print("-------------------------------------------------------")
            break
        else:
            print("   Sorry, the number needs to be between 1 and 10")
    else:
        print("   Sorry, no letters and no numbers below 1 or higher than 10")
        continue


def get_board_size():
    """
    Y is the global variable for the board size.
    This function creates the rows.
    """
    for x in range(Y):
        BOARD.append(["-"] * Y)
    return Y


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def print_board():
    """
    Creates the board and prints it.
    """
    letters = ALPHABET[0: (Y)]
    print("      %s%s" % (" ", " ".join(letters)))
    row_number = 1
    for row in BOARD:
        if row_number <= 9:
            print("     %d|%s|" % (row_number, "|".join(row)))
        else:
            print("    %d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def making_ships():
    """
    Placing the ships on the board.
    """
    ships_placed = 0
    global TOTAL_SHIPS
    if Y <= 3:
        TOTAL_SHIPS = 1
        while ships_placed != TOTAL_SHIPS:
            ship_row = randint(1, (Y))
            ship_col = randint(1, (Y))
            ship_location = [ship_row, ship_col]
            SHIP_PLACEMENT.append(ship_location)
            ships_placed += 1
    elif Y < 8 and Y > 3:
        TOTAL_SHIPS = 3
        while ships_placed != TOTAL_SHIPS:
            ship_row = randint(1, (Y))
            ship_col = randint(1, (Y))
            ship_location = [ship_row, ship_col]
            SHIP_PLACEMENT.append(ship_location)
            ships_placed += 1
    else:
        TOTAL_SHIPS = 10
        while ships_placed != TOTAL_SHIPS:
            ship_row = randint(1, (Y))
            ship_col = randint(1, (Y))
            ship_location = [ship_row, ship_col]
            SHIP_PLACEMENT.append(ship_location)
            ships_placed += 1
    # print(ship_placement)
    # un-comment this if you want to see where the ships are placed.


def making_guesses():
    """
    This function will take input from the user.
    Check the input against the placement of this ships.
    Record the guess and give output through the terminal.
    Changes the board according to hit or miss.
    """
    global SHIPS_SUNK
    for turn in range((Y*Y) // 2):
        shots = int((Y*Y) // 2)
        print(" ")
        print(f'  Lieutenant: "Commander, we have {shots - turn} shots left."')
        print('  Commander: "And How many ships are left Lieutenant?"')
        print(f'  Lieutenant: "{TOTAL_SHIPS - SHIPS_SUNK} left Commander."')
        guess_col = None
        while True:
            guess_col = input("  Enter column letter: ")
            if guess_col.isalpha() and len(guess_col) == 1:
                guess_col = guess_col.lower()
                guess_col = ord(guess_col) - 96
                break
            else:
                print_board()
                print(" Commander, the available letters are on the board....")
                continue
        guess_row = None
        while True:
            guess_row = input("  Enter a row number: ")
            if guess_row.isdigit():
                guess_row = int(guess_row)
                break
            else:
                print_board()
                print("  Commander, what you have entered is not in range...")
                continue
        g_row = guess_row
        g_col = guess_col
        guess = [g_row, g_col]
        if guess in SHIP_PLACEMENT:
            print("-------------------------------------------------------")
            print("          Commander! You sunk a battleship!")
            print("-------------------------------------------------------")
            BOARD[g_row - 1][g_col - 1] = "O"
            SHIPS_SUNK += 1
        elif (turn + 1) - shots == 0:
            print("-------------------------------------------------------")
            print("                   Game Over..")
            print("   Lets go back to the docks and restock ammunition")
            print("-------------------------------------------------------")
        elif (g_row < 1 or g_row > Y) or (g_col < 1 or g_col > Y):
            print("-------------------------------------------------------")
            print("     Commander, your coordinates are out of range!")
            print("              Stop wasting our shots!")
            print(f"          Try shooting within rows: 1-{Y}")
            print(f"          And columns: A-{ALPHABET[Y - 1]}")
            print("-------------------------------------------------------")
        elif (BOARD[g_row - 1][g_col - 1]) == "X":
            print("-------------------------------------------------------")
            print("      Commander...You guessed that one already...")
            print("-------------------------------------------------------")
        elif (BOARD[g_row - 1][g_col - 1]) == "O":
            print("-------------------------------------------------------")
            print("      Commander...You guessed that one already...")
            print("-------------------------------------------------------")
        else:
            print("-------------------------------------------------------")
            print(" Commander, you missed the battleship, let's try again!")
            print("-------------------------------------------------------")
            BOARD[g_row - 1][g_col - 1] = "X"
        if SHIPS_SUNK == TOTAL_SHIPS:
            print_board()
            print("-------------------------------------------------------")
            print("Congratulations Commander, you have sunk all the ships!")
            print("   Victory is ours, set sails, and let's go home!")
            print("-------------------------------------------------------")
            break
        print_board()
    turn += 1


def run_game():
    """
    This runs the entire game in order
    """
    get_board_size()
    print("               Let's play Battleships!")
    print("-------------------------------------------------------")
    print(" ")
    print_board()
    making_ships()
    making_guesses()


def restart_game():
    """
    This function allows us to restart the game or quit the terminal.
    """
    play = input("Type yes to play again and no to quit: ").lower()
    while True:
        if play == "no":
            exit()
        elif play == "yes":
            # This restart code was found at StackOverflow
            print("------------------------------------")
            print("argv was", sys.argv)
            print("sys.executable was", sys.executable)
            print("restart now")
            print("------------------------------------")
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            print("please type either yes or no")
            restart_game()


# These are global variables used throughout the code
Y = BOARD_SIZE
BOARD = []
SHIP_PLACEMENT = []
TOTAL_SHIPS = 10
SHIPS_SUNK = 0

run_game()
restart_game()
