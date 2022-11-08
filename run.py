# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


print("Welcome to the game of Battleships!")

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
    return [["_" for count in range(board_columns)] for rows in range(board_rows)]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("")

def test():
    myboard = create_board(board_rows, board_columns)
    # print_board(myboard)
    myboard[1][2] = str(6)
    print_board(myboard)

test()



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
