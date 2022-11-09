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
