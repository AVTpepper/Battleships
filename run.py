# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


print("Welcome to the game of Battleships!")
"""
# board = []

print("""
    We want you to create a custom Battleship board.\n
    Normally a Battleship board consists of 10 rows and 10 columns.\n
    This time, you get to decide the battlefield.\n
    After every input you type into the game, press enter to continue.
    """)
board_rows = int(input("Type the amount of rows you would like to play with: "))
# board_rows_confirm = input(f"You have selected {board_rows}. Would you like to continue? y/n: ")
board_columns = int(input("Type the amount of columns you would like to play with: "))

def create_board(board_rows, board_columns):
    """
    Creates the board based on user input
    """
    return [["_" for count in range(board_columns)] for row in range(board_rows)]


for i in range(1, board_columns+1):
        print(i, end="")


def game_board(myboard):
    
        #num = 1
    #while num <= board_columns:
        #print("    " + str(num))
        #num += 1
    #print("    0    1    2")
    for count, row in enumerate(myboard):
        print(count, row)


def test():
    myboard = create_board(board_rows, board_columns)
    # print_board(myboard)
    myboard[1][2] = str(6)
    game_board(myboard)
    # print_board(myboard)
    

test()


board = []

for x in range(board_columns):
    board.append(["_" * board_columns])

def create_board(board):
    print(" ", " ".join(""))

board = []

def create_board_v2():
    for row in range(board_rows):
        board.append([])
        for column in range(board_columns):
            board[row].append("_")
    y = " "
    xy = y.join(row)
    print(xy)

create_board_v2()

# for x in range(0, board_rows):
    # board.append(["_ " * board_rows])

# print(board)


# def create_board(board):
    # for row in board:
        # print((" ").join(row))


# create_board(board)
        
    #return [["_" for count in range(board_columns)] for count in range(board_rows)]

#print(create_board(board_rows, board_columns))

#create_board(board_rows, board_columns)

letters = []
board = []
i = 0
while i < 5:
    board_block = ("_")*1
    board.append(board_block)
    
    i += 1
print(board)



game_board = " ".join(str(item) for item in board)
print(game_board)

rows = (game_board + "\n") * 5

print(rows)

for first_index in board:
"""
--------------------------------------------------
"""
letters = []
board = []
i = 0
while i < 5:
    board_block = ("_")*1
    board.append(board_block)
    def upperCaseAlphabets():
        print("Upper Case Alphabets")
        for i in range(65, (65+5)):
            print(chr(i), end=" ")
    i += 1




game_board = " ".join(str(item) for item in board)

rows = ("\n" + game_board + "\n") + (game_board + "\n") * 4

#for first_index in board

def upperCaseAlphabets():
    print("Upper Case Alphabets")
    for i in range(65, (65+5)):
        print(chr(i), end=" ")

upperCaseAlphabets()
#print(board)
#print(game_board)
print(rows)
"""
"""
This code also works to create a list of lists

row = int(input("enter number of rows: "))

column = int(input("enter number of columns: "))
rows = []

def create_rows():
    i=0
    while i < row:
        piece = str(i) + " " + ("_ " * column)
        rows.append(piece)
        i+=1
    print(rows)

create_rows()
"""

row = int(input("enter number of rows: "))

column = int(input("enter number of columns: "))
rows = []
columns = []

def create_board():
    i=1
    while i < (row + 1):
        piece = str(i) + " " + ("_   " * column)
        rows.append(piece)
        i+=1
        game_board = "\n".join(str(item) for item in rows)
    print(game_board)

def create_column_index():
    i=1
    while i < (column + 1):
      col_number = "  " + str(i)
      columns.append(col_number)
      i += 1
      indexes = " ".join(str(index) for index in columns)
    print(indexes)
    

    
create_column_index()    
create_board()
