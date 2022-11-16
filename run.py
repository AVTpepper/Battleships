#guess_row = None
#while True:
#    guess_row = input("Enter a row number: ")

#    if guess_row.isdigit():
#        guess_row = int(guess_row)
#        break
#    else:
#        print("please enter a number")
#        continue



alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

board_size = 10
while True:
    guess_col = input("Enter column letter: ")

    if guess_col.isalpha() and len(guess_col) == 1:
        guess_col = guess_col.lower()
        guess_col = ord(guess_col) - 96
        print(guess_col)

        if guess_col in range(1, board_size):
            print("that works")
            print(guess_col)
            break
        #guess_col = ord(guess_col) -96
            print("that works")
            print(guess_col)
        else:
            print("that didnt work either")
            continue
    else:
        print("that didnt work")
        continue
