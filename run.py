# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


print("Welcome to the game of Battleships!")


print("""
    We want you to create a custom Battleship board.\n
    Normally a Battleship board consists of 10 rows and 10 columns.\n
    This time, you get to decide the size of the battlefield.\n
    After every input you type into the game, press enter to continue.
    """)


row = int(input("enter number of rows: "))

column = int(input("enter number of columns: "))
rows = []
columns = []

def create_board():
    i = 1
    while i < (row + 1):
        piece = str(i) + " " + ("-   " * column)
        rows.append(piece)
        i+=1
        game_board = "\n".join(str(item) for item in rows)
    print(game_board)


def create_column_index():
    i = 1
    while i < (column + 1):
        col_number = "  " + str(i)
        columns.append(col_number)
        i += 1
        indexes = " ".join(str(index) for index in columns)
    print(indexes)


create_column_index()    
create_board()

"""
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
