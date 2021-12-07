
def letter_to_number(letter):
    letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    return letters_to_numbers.get(letter)

def changing_table(row, col, board):
        board[row][col] = "X"
        return board

def stawianie_statkow_na_planszy():
    user_input = input("Choose coordinates: ")
    while len(user_input) != 2:
        user_input = input("Wrong!! Try again!: ")
    letter1 = user_input[0]
    row = letter_to_number(letter1)
    col = user_input[1]
    return row, col


def podstawienie_znakow(user1_input):

    pass
