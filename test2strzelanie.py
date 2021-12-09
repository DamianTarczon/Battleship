from tabulate import tabulate
import copy

def get_list_copy(list):
    new_list = copy.deepcopy(list)
    return new_list


def letter_to_number(letter):
    letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    return letters_to_numbers.get(letter)

def changing_table(row, col, board, value = "X"):
        board[row][col] = value

def check_valid_move_from_user_input():
    letters = ["A", "B", "C", "D", "E"]
    numbers = ["1", "2", "3", "4", "5"]
    user_input = input("Choose coordinates: ").upper()
    while True:
        if len(user_input) != 2:
            print('Wrong! Your input should be like this a1')
            user_input = input("Wrong! Choose again: ").upper()
            continue
        elif user_input[0] not in letters:
            print('First mark can only be a,b,c,d,e.')
            user_input = input("Wrong! Choose again: ").upper()
            continue
        elif user_input[1] not in numbers:
            print('Second mark can only be 1,2,3,4,5.')
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

def print_table2(list1, list2):
    head = [" ", "1", "2", "3", "4", "5", " ", " ", "1", "2", "3", "4", "5"]
    print_arr = []
    for index, _ in enumerate(list1):
        row = list1[index] + [" "] + list2[index]
        print_arr.append(row)
        
    print(tabulate(print_arr, head , tablefmt="fancy_grid"))



def check_move_1_for_2flag_ship(row, col, board):
    while True:
        user_input = check_valid_move_from_user_input()
        row2, col2 = user_input_to_row_and_col(user_input)
        if row2 == row - 1 and col2 == col:
            changing_table(row2, col2, board)
            break
        elif row2 == row + 1 and col2 == col:
            changing_table(row2, col2, board)
            break
        elif row2 == row and col2 == col - 1:
            changing_table(row2, col2, board)
            break
        elif row2 == row and col2 == col + 1:
            changing_table(row2, col2, board)
            break
        else:
            print('Your move can only be upright or horizontal')
            continue


def check_move_2_for_2flag_ship(board):
    while True:
        try:
            user_input = check_valid_move_from_user_input()
            row, col = user_input_to_row_and_col(user_input)
            if board[row-1][col] == "X":
                ('Your ship is too close to another. ')
                continue
            elif board[row][col - 1] == "X":
                ('Your ship is too close to another. ')
                continue
            elif board[row][col + 1] == "X":
                ('Your ship is too close to another. ')
                continue
            elif board[row + 1][col] == "X":
                ('Your ship is too close to another. ')
                continue
            else:
                changing_table(row, col, board)
                return row, col
        except:
            changing_table(row, col, board)
            return row, col


def check_move_3_for_2flag_ship(row, col, board):
    while True:
        try:
            user_input = check_valid_move_from_user_input()
            row3, col3 = user_input_to_row_and_col(user_input)
            if row3 == row - 1 and col3 == col:
                if board[row3-1][col3] == "X":
                    ('Your ship is too close to another. ')
                    continue
                elif board[row3][col3 - 1] == "X":
                    ('Your ship is too close to another. ')
                    continue
                elif board[row3][col3 + 1] == "X":
                    ('Your ship is too close to another. ')
                    continue
                else:
                    changing_table(row3, col3, board)
                break  
            elif row3 == row + 1 and col3 == col:
                if board[row3][col3 - 1] == "X":
                    ('Your ship is too close to another. ')
                    continue
                elif board[row3][col3 + 1] == "X":
                    ('Your ship is too close to another. ')
                    continue
                elif board[row3 + 1][col3] == "X":
                    ('Your ship is too close to another. ')
                    continue
                else:
                    changing_table(row3, col3, board)
                break
            elif row3 == row and col3 == col - 1:
                if board[row3-1][col3] == "X":
                    ('Your ship is too close to another. ')
                    continue
                elif board[row3][col3 - 1] == "X":
                    ('Your ship is too close to another. ')
                    continue
                elif board[row3 + 1][col3] == "X":
                    ('Your ship is too close to another. ')
                    continue
                else:
                    changing_table(row3, col3, board)
                break
            elif row3 == row and col3 == col + 1:
                if board[row3-1][col3] == "X":
                    ('Your ship is too close to another. ')
                    continue
                elif board[row3][col3 + 1] == "X":
                    ('Your ship is too close to another. ')
                    continue
                elif board[row3 + 1][col3] == "X":
                    ('Your ship is too close to another. ')
                    continue
                else:
                    changing_table(row3, col3, board)
                break
            else:
                continue
        except:
            changing_table(row3, col3, board)
            break


def check_move_4_for_1flag_ship(board):
    while True:
        try:
            user_input = check_valid_move_from_user_input()
            row, col = user_input_to_row_and_col(user_input)
            if board[row-1][col] == "X":
                ('Your ship is too close to another. ')
                continue
            elif board[row][col - 1] == "X":
                ('Your ship is too close to another. ')
                continue
            elif board[row][col + 1] == "X":
                ('Your ship is too close to another. ')
                continue
            elif board[row + 1][col] == "X":
                ('Your ship is too close to another. ')
                continue
            else:
                changing_table(row, col, board)
                break
        except:
            changing_table(row, col, board)
            break
    


def podstawienie_znakow(board):
    print_table(board)
    user_input = check_valid_move_from_user_input()
    row, col = user_input_to_row_and_col(user_input)
    changing_table(row, col, board)
    print_table(board)
    check_move_1_for_2flag_ship(row, col, board)
    print_table(board)
    row2, col2 = check_move_2_for_2flag_ship(board)
    print_table(board)
    check_move_3_for_2flag_ship(row2, col2, board)
    print_table(board)
    check_move_4_for_1flag_ship(board)
    print_table(board)
    check_move_4_for_1flag_ship(board)
    print_table(board)


def check_user_shoot(row, col, board, board_for_shooting):
    if board[row][col] == "X":
        if board_for_shooting[row-1][col] == "H":
            board_for_shooting[row-1][col] = "S"
            return "S"
        elif board_for_shooting[row][col - 1] == "H":
            board_for_shooting[row][col - 1] = "S"
            return "S"
        elif board_for_shooting[row][col + 1] == "H":
            board_for_shooting[row][col + 1] = "S"
            return "S"
        elif board_for_shooting[row + 1][col] == "H":
            board_for_shooting[row + 1][col] = "S"
            return "S"
        else:
            return "H"
    elif board[row][col] != "X":
        return "M"


def user_is_shooting(board, board_for_shooting):
    user_input = check_valid_move_from_user_input()
    row, col = user_input_to_row_and_col(user_input)
    shoot_value = check_user_shoot(row, col, board, board_for_shooting)
    changing_table(row, col, board_for_shooting, shoot_value)


def main():
    board = [["A", 0, 0, 0, 0, 0], ["B", 0, 0, 0, 0, 0], ["C", 0, 0, 0, 0, 0], ["D", 0, 0, 0, 0, 0], ["E", 0, 0, 0, 0, 0]]
    board_for_shooting = get_list_copy(board)
    podstawienie_znakow(board)
    print_table2(board, board_for_shooting)
    user_is_shooting(board, board_for_shooting)
    print_table2(board, board_for_shooting)
    user_is_shooting(board, board_for_shooting)
    print_table2(board, board_for_shooting)

main()

    