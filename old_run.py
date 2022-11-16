# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint





    

print("Welcome to the game of Battleships!")
print("We want you to create a custom Battleship board.")
print("Normally a Battleship board consists of 10 rows and 10 columns.")
print("This time, you get to decide the size of the battlefield.")
print("After every input you type into the game, press enter to continue.")
board_size = int(input("enter board size: "))


def get_board_size():
        
    global y
    global board

    if y > 1 and y <= 10:
        print("perfect")
    if y < 1 or y > 10:
        raise Exception("Sorry, no numbers below 1 or higher than 10")

    for x in range(y):
        board.append(["-"] * y)
    return y


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def print_board():
    """
    creates the board
    """
    global board
    letters = alphabet[0: (y)]
    print("  %s%s" % (" "," ".join(letters)))
    row_number = 1
    for row in board:
        if row_number <= 9:
            print(" %d|%s|" % (row_number, "|".join(row)))
        else:
            print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def making_ships():
    global y
    global board
    global ship_placement
    ships_placed = 0
    global ships_sunk
    global total_ships
    shots = 20
    if y <= 3:
        shots = 2
        total_ships = 1
        print(f"There is {total_ships} ship in range commander, go shoot it down!")
        while ships_placed != total_ships:
            ship_row = randint(1, (y))
            ship_col = randint(1, (y))
            ship_location = [ship_row, ship_col]
            ship_placement.append(ship_location)
            ships_placed += 1
    elif y < 6 and y > 3 :
        total_ships = 3
        shots = 10
        print(f"There are {total_ships} ships in range commander, go shoot them down!")
        while ships_placed != total_ships:
            ship_row = randint(1, (y))
            ship_col = randint(1, (y))
            ship_location = [ship_row, ship_col]
            ship_placement.append(ship_location)
            ships_placed += 1
    else:
        shots = 20
        total_ships = 10
        print(f"There are {total_ships} ships in range commander, go shoot them down!")
        while ships_placed != total_ships:
            ship_row = randint(1, (y))
            ship_col = randint(1, (y))
            ship_location = [ship_row, ship_col]
            ship_placement.append(ship_location)
            ships_placed += 1
    print(ship_placement)
   
        
def making_guesses():
    global ship_placement
    global ships_sunk
    global board_size
    global total_ships
    
    for turn in range((y*y) // 3):  
            # I want this to be in a second function, 
            # but Im stuck at how I can do that because of the variables 
            # I am using I have tried passing them through return___ and having them in paranthesis behind the def function(__)
        shots = (y*y) // 3
        print(f"Commander, we have {shots - turn} shots left.")
        print(f"Our scouting report says there are this many ships left: {total_ships - ships_sunk} ")
                
                
        guess_row = None
        while True:
            guess_row = input("Enter a row number: ")

            if guess_row.isdigit():
                guess_row = int(guess_row)
                break
            else:
                print("Commander, what you have entered is not in range...")
                continue

        guess_col = None
        while True:
            guess_col = input("Enter column letter: ")

            if guess_col.isalpha() and len(guess_col) == 1:
                guess_col = guess_col.lower()
                guess_col = ord(guess_col) - 96
                print(guess_col)
                break

                #if guess_col in range(1, board_size):
                #    print("that works")
                #    print(guess_col)
                    #break
                #guess_col = ord(guess_col) -96
                #    print("that works")
                #    print(guess_col)
                #else:
                #    print("Please enter a letter thats visible on the board")
                #    continue
            else:
                print("Commander, the available letters are on the board!")
                continue

        print(f"Shots {shots}")
        guess = [guess_row, guess_col]
        if guess in ship_placement:
            print("Commander! You sunk a battleship!")
            board[guess_row - 1][guess_col - 1] = "O"
            ships_sunk += 1
        elif (turn + 1) - shots == 0:
            print("Game Over, lets go back to the docks and restock ammunition")
            #break
        elif (guess_row < 1 or guess_row > y) or (guess_col < 1 or guess_col > y):
            print("Commander, your coordinates are out of range!")
            print("Stop wasting our shots!")
            print(f"Try shooting within rows 1-{y} and columns A-{alphabet[y - 1]}")
        elif (board[guess_row - 1][guess_col - 1]) == "X" or (board[guess_row - 1][guess_col - 1]) == "O":
            print("Commander...You guessed that one already...")
        else:
            print("Commander, you missed the battleship, let's try again!")
            board[guess_row - 1][guess_col - 1] = "X"
        if ships_sunk == total_ships:
            print_board()
            print("Congratulations Commander, you have sunk all the ships!")
            print("Victory is ours, set sails, and let's go home!")
            break 
        turn += 1
                
        print_board()

    


def run_game():
    global y
    get_board_size()
    print("Let's play Battleship!")
    print_board()
    making_ships()
    making_guesses()

def restart_game():
    print("hello!")
    play = input("Type yes to play again and no to quit: ").lower()
    while True:
        if play == "no":
            exit()
        elif play == "yes":
            import sys
            print("------------------------------------")
            print("argv was",sys.argv)
            print("sys.executable was", sys.executable)
            print("restart now")

            import os
            os.execv(sys.executable, ['python'] + sys.argv)
            print("------------------------------------")
        else: 
            print("please type either yes or no")
            restart_game()


y = board_size
board = []
ship_placement = []
total_ships = 10
print(total_ships)
ships_sunk = 0

run_game()
restart_game()

y = board_size







