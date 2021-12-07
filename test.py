from tabulate import tabulate


def letter_to_number(letter):
    letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    return letters_to_numbers.get(letter)

def changing_table(row, col, board):
        board[row][col] = "X"

def check_valid_move_from_user_input():
    letters = ["A", "B", "C", "D", "E"]
    numbers = ["1", "2", "3", "4", "5"]
    user_input = input("Choose coordinates: ").upper()
    while True:
        if len(user_input) != 2:
            user_input = input("Wrong! Choose again: ").upper()
            continue
        elif user_input[0] not in letters:
            user_input = input("Wrong! Choose again: ").upper()
            continue
        elif user_input[1] not in numbers:
            user_input = input("Wrong! Choose again: ").upper()
            continue
        else:
            return user_input

def user_input_to_row_and_col(user_input):
    letter1 = user_input[0]
    row = letter_to_number(letter1)
    col = int(user_input[1])
    return row, col

def print_table(list):
    head = [" ", "1", "2", "3", "4", "5"]
    print(tabulate(list, headers=head, tablefmt="fancy_grid"))

def check_move_1(row, col, board):
    '''board[row - 1][col] #nad x
    board[row][col - 1] #po lewej stronie x
    board[row][col + 1] #po prawej stronie x
    board[row + 1][col] #pod x'''
    while True:
        user_input = check_valid_move_from_user_input()
        row2, col2 = user_input_to_row_and_col(user_input)
        if board[row2][col2] == board[row - 1][col]:
            changing_table(row2, col2, board)
            break
        elif board[row2][col2] == board[row + 1][col]:
            changing_table(row2, col2, board)
            break
        elif board[row2][col2] == board[row][col - 1]:
            changing_table(row2, col2, board)
            break
        elif board[row2][col2] == board[row][col + 1]:
            changing_table(row2, col2, board)
            break
        else:
            continue


def podstawienie_znakow(board):
    print_table(board)
    user_input = check_valid_move_from_user_input()
    row, col = user_input_to_row_and_col(user_input)
    changing_table(row, col, board)
    print_table(board)
    check_move_1(row, col, board)
    print_table(board)

    #check_move_1()


board = [["A", 0, 0, 0, 0, 0], ["B", 0, 0, 0, 0, 0], ["C", 0, 0, 0, 0, 0], ["D", 0, 0, 0, 0, 0], ["E", 0, 0, 0, 0, 0]]

podstawienie_znakow(board)
