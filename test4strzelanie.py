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
        user_input = check_valid_move_from_user_input()
        row, col = user_input_to_row_and_col(user_input)
        value = is_empty_or_out_of_range(board, row-1, col)
        if value == "N":
            continue
        value = is_empty_or_out_of_range(board, row, col-1)
        if value == "N":
            continue
        value = is_empty_or_out_of_range(board, row, col+1)
        if value == "N":
            continue
        value = is_empty_or_out_of_range(board, row+1, col)
        if value == "N":
            continue
        else:
            changing_table(row, col, board)
            return row, col

    '''while True:
        try:
            user_input = check_valid_move_from_user_input()
            row, col = user_input_to_row_and_col(user_input)
            if board[row-1][col] == "X":
                continue
            elif board[row][col - 1] == "X":
                continue
            elif board[row][col + 1] == "X":
                continue
            elif board[row + 1][col] == "X":
                continue
            else:
                changing_table(row, col, board)
                return row, col
        except:
            changing_table(row, col, board)
            return row, col'''

def is_in_board(board, row, col):
    if (len(board) > row and 0 <= row) and (len(board[0]) > col and 1 <= col):
        return True
    return False

def check_move_3_for_2flag_ship(row, col, board):
    while True:
        user_input = check_valid_move_from_user_input()
        row_for_second_x, col_for_second_x = user_input_to_row_and_col(user_input)
        if is_in_board(board, row-1, col) and row_for_second_x == row-1 and col_for_second_x == col:
            value = is_empty_or_out_of_range(board, row_for_second_x-1, col_for_second_x)
            if value == "N":
                continue
            value = is_empty_or_out_of_range(board, row_for_second_x, col_for_second_x-1)
            if value == "N":
                continue
            value = is_empty_or_out_of_range(board, row_for_second_x, col_for_second_x+1)
            if value == "N":
                continue
            #value = is_empty_or_out_of_range(board, row_for_second_x+1, col_for_second_x)
            #if value == "N":
                #continue

            changing_table(row_for_second_x, col_for_second_x, board)
            break

        elif is_in_board(board, row, col-1) and row_for_second_x == row and col_for_second_x == col-1:
            value = is_empty_or_out_of_range(board, row_for_second_x-1, col_for_second_x)
            if value == "N":
                continue
            value = is_empty_or_out_of_range(board, row_for_second_x, col_for_second_x-1)
            if value == "N":
                continue
            #value = is_empty_or_out_of_range(board, row_for_second_x, col_for_second_x+1)
            #if value == "N":
                #continue
            value = is_empty_or_out_of_range(board, row_for_second_x+1, col_for_second_x)
            if value == "N":
                continue
            changing_table(row_for_second_x, col_for_second_x, board)
            break
        elif is_in_board(board, row, col+1) and row_for_second_x == row and col_for_second_x == col+1:
            value = is_empty_or_out_of_range(board, row_for_second_x-1, col_for_second_x)
            if value == "N":
                continue
            #value = is_empty_or_out_of_range(board, row_for_second_x, col_for_second_x-1)
            #if value == "N":
                #continue
            value = is_empty_or_out_of_range(board, row_for_second_x, col_for_second_x+1)
            if value == "N":
                continue
            value = is_empty_or_out_of_range(board, row_for_second_x+1, col_for_second_x)
            if value == "N":
                continue
            changing_table(row_for_second_x, col_for_second_x, board)
            break
        elif is_in_board(board, row+1, col) and row_for_second_x == row+1 and col_for_second_x == col:
            #value = is_empty_or_out_of_range(board, row_for_second_x-1, col_for_second_x)
            #if value == "N":
                #continue
            value = is_empty_or_out_of_range(board, row_for_second_x, col_for_second_x-1)
            if value == "N":
                continue
            value = is_empty_or_out_of_range(board, row_for_second_x, col_for_second_x+1)
            if value == "N":
                continue
            value = is_empty_or_out_of_range(board, row_for_second_x+1, col_for_second_x)
            if value == "N":
                continue
            changing_table(row_for_second_x, col_for_second_x, board)
            break
        else:
            continue
    '''while True:
        try:
            user_input = check_valid_move_from_user_input()
            row3, col3 = user_input_to_row_and_col(user_input)
            if row3 == row - 1 and col3 == col:
                if board[row3-1][col3] == "X":
                    continue
                elif board[row3][col3 - 1] == "X":
                    continue
                elif board[row3][col3 + 1] == "X":
                    continue
                else:
                    changing_table(row3, col3, board)
                break  
            elif row3 == row + 1 and col3 == col:
                if board[row3][col3 - 1] == "X":
                    continue
                elif board[row3][col3 + 1] == "X":
                    continue
                elif board[row3 + 1][col3] == "X":
                    continue
                else:
                    changing_table(row3, col3, board)
                break
            elif row3 == row and col3 == col - 1:
                if board[row3-1][col3] == "X":
                    continue
                elif board[row3][col3 - 1] == "X":
                    continue
                elif board[row3 + 1][col3] == "X":
                    continue
                else:
                    changing_table(row3, col3, board)
                break
            elif row3 == row and col3 == col + 1:
                if board[row3-1][col3] == "X":
                    continue
                elif board[row3][col3 + 1] == "X":
                    continue
                elif board[row3 + 1][col3] == "X":
                    continue
                else:
                    changing_table(row3, col3, board)
                break
            else:
                continue
        except:
            changing_table(row3, col3, board)
            break'''


def check_move_4_for_1flag_ship(board):
    while True:
        user_input = check_valid_move_from_user_input()
        row, col = user_input_to_row_and_col(user_input)
        value = is_empty_or_out_of_range(board, row-1, col)
        if value == "N":
            continue
        value = is_empty_or_out_of_range(board, row, col-1)
        if value == "N":
            continue
        value = is_empty_or_out_of_range(board, row, col+1)
        if value == "N":
            continue
        value = is_empty_or_out_of_range(board, row+1, col)
        if value == "N":
            continue
        else:
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


def check_x_all_around(board, row, col):
    try:
        if board[row-1][col] == "X":
            return "H"
        elif board[row][col - 1] == "X":
            return "H"
        elif board[row][col + 1] == "X":
            return "H"
        elif board[row + 1][col] == "X":
            return "H"
        else:
            return "S"
    except:
        return "S"


def is_empty_or_out_of_range(board, row, col):
    if (len(board) > row and 0 <= row) and (len(board[0]) > col and 1 <= col):
        if board[row][col] == 0:
            return "Y"
        return "N"
    return "Y"


'''def is_empty_or_out_of_range(board, row, col):
    if (len(board) > row and 0 < row) and (len(board[0]) > col and 1 <= col):
        if board[row][col] == 0:
            return True
        return False
    return False'''

'''def is_out_of_range(board, row, col):
    if (len(board) > row or 0 >= row) and (len(board[0]) > col or 1 >= col):
        return True
    return False'''

'''def is_x(board, row, col):
    if board[row][col] == "X":
        return True
    return False'''

def is_h_or_out_of_range(board, row, col):
    if (len(board) > row or 0 >= row) and (len(board[0]) > col or 1 >= col):
        if board[row][col] == "H":
            board[row][col] = "S"
            return "S"
        return "N"
    return "N"
        

def check_user_shoot(row, col, board, board_for_shooting):
    if board[row][col] == "X":
        value = check_x_all_around(board, row, col)
        if value == "S":
            return "S"
        else:
            value1 = is_h_or_out_of_range(board_for_shooting, row-1, col)
            if value1 != "N":
                return value1
            value2 = is_h_or_out_of_range(board_for_shooting, row, col-1)
            if value2 != "N":
                return value2
            value3 = is_h_or_out_of_range(board_for_shooting, row, col+1)
            if value3 !="N":
                return value3
            value4 = is_h_or_out_of_range(board_for_shooting, row+1, col)
            if value4 != "N":
                return value4
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
    print_table(board_for_shooting)
    user_is_shooting(board, board_for_shooting)
    print_table(board_for_shooting)
    user_is_shooting(board, board_for_shooting)
    print_table(board_for_shooting)
    user_is_shooting(board, board_for_shooting)
    print_table(board_for_shooting)
    user_is_shooting(board, board_for_shooting)
    print_table(board_for_shooting)

main()

'''if is_out_of_range(board_for_shooting, row-1, col):
            if is_x(board, row-1, col):
                return "H"
        elif is_out_of_range(board_for_shooting, row, col-1):
            if is_x(board, row, col-1):
                return "H"
        elif is_out_of_range(board_for_shooting, row, col+1):
            if is_x(board, row, col+1):
                return "H"
        elif is_out_of_range(board_for_shooting, row+1, col):
            if is_x(board, row+1, col):
                return "H"
        else:
            return "S"'''