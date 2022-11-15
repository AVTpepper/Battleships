# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


print("Welcome to the game of Battleships!")


print("We want you to create a custom Battleship board.15")
print("Normally a Battleship board consists of 10 rows and 10 columns.")
print("This time, you get to decide the size of the battlefield.")
print("After every input you type into the game, press enter to continue.")
#add print message specifying that the board needs to be 10 or less.

#enter board size instead of rows and columns. 3 = 3x3, 4 = 4x4
board_size = int(input("enter board size: ")) 
#check what is entered, with a message, higher that max, enter something less than or 10

board = []

for x in range(board_size):
    board.append(["-"] * board_size)

print(board)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def print_board(board):
    column = 0
    #for column in board:
        # index = "  " + alphabet[range(len(board))]
    #column += 1
    #print(index)
    letters = alphabet[0: (board_size)]
    print(letters)
    #for i in letters:
    print(" %s%s" % (" "," ".join(letters)))


    #range(len(board))
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
       # print(" +-+-+-+-+-+")
        row_number += 1    
        #for letter in alphabet:

"""
i = 1
    while i < (column + 1):
        col_number = "   " + str(i)
        columns.append(col_number)
        i += 1
        indexes = " ".join(str(index) for index in columns)
    print(indexes)
"""

     # print(" "+ )
    #print("  " + alphabet[0: len(board)] + "  ")
    #print(" +-+-+-+-+-+")
    

print("Let's play Battleship!")
print_board(board)



"""
column = int(input("enter number of columns: "))

rows = []
columns = []
game_board = " "



def create_board():
    i = 1
    while i < (row + 1):
        piece = str(i)
        dash = "-"
        list_creation = [piece] + ([dash] * column)
        rows.append(list_creation)
        i+=1
        game_board = "\n".join(str(item) for item in rows)
    create_column_index()
    print(game_board)
    # print(rows)



def create_column_index():
    i = 1
    while i < (column + 1):
        col_number = "   " + str(i)
        columns.append(col_number)
        i += 1
        indexes = " ".join(str(index) for index in columns)
    print(indexes)

def update_board(rows):
    #guess_row = [int(input("enter row: "))]
    #guess_column=[int(input("enter column: "))]
    #guess = guess_row + guess_column
    #print(guess)
    #guesses = []
    rows[(int(input("enter row: ")))-1][int(input("enter column: "))] = "O"
    

    
    # create_column_index()
    # create_board()
    # create_board()
# rows[1][2] = "X"
# print(game_board)


# def place_ships():


# def shots():


# def run_game():

# create_column_index()    
create_board()

rows[1][2]= "X"
# print(rows)
update_board(rows)
# create_column_index()
# create_board()


Another try at creating a functional board
"""

"""
row = int(input("Enter rows here: "))
column = int(input("enter columns here: "))

#Hidden_Board = [["-"]*


Hidden_Pattern= [[' ']*8 for x in range(8)]
Guess_Pattern= [[' ']*8 for x in range(8)]

#print(Hidden_Pattern)

Hidden_Board = [[" "]*row for x in range(column+1)]
Board = [[" "]*row for x in range(column+1)]


letters_to_number = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10}

def print_board(Board):
  letters=["A","B","C","D","E","F","G","H","I","J","K"]
  column_letters=[]
  i = 0
  while i < column:
    column_letters.append(letters[i])
    i +=1
  print(column_letters)
  #print(Board)
  row_num = 1
  for row in Board:
    print(row_num, "|-|".join(row))
    row_num += 1
    
print_board(Board)
"""
