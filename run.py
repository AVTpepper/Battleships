# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


print("Welcome to the game of Battleships!")

board = []


def create_board(board):
    print("""
    We want you to create a custom Battleship board.\n
    Normally a Battleship board consists of 10 rows and 10 columns.\n
    This time, you get to decide the battlefield.\n
    After every input you type into the game, press enter to continue.
    """)
    board_rows = int(input("Type the amount of rows you would like to play with: "))
    board_rows_confirm = input(f"You have selected {board_rows}. Would you like to continue? y/n: ")
    board_columns = int(input("Type the amount of columns you would like to play with: "))
    
    for row in range(board_rows):
        board.append(["_"] * board_columns)
    # print(board)
    letter = 0
    for letter in range(board_rows):
        print(chr(letter + 65), end = " | ")
        for column in range(board_columns):
            print(board[letter][column], end = " ")
        letter += 1
        

create_board(board)

print(board[A,1])