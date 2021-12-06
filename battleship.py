from tabulate import tabulate
import copy


def changing_table(player, player_move, list):
    if len(player_move) == 2:
        row = int(player_move[1])
        column = letter_to_number(player_move[0])
        list[column][row] = player
        return list

def letter_to_number(letter):
    if letter == "A":
        return 0
    elif letter == "B":
        return 1
    elif letter == "C":
        return 2


def print_table(list):
    head = [" ", "1", "2", "3"]
    return(tabulate(list, headers=head, tablefmt="fancy_grid"))


def get_list_copy(list):
    new_list = copy.deepcopy(list)
    return new_list


def check_move(list):
    move_dict = {
        "A1": list[0][1],
        "A2": list[0][2],
        "A3": list[0][3],
        "B1": list[1][1],
        "B2": list[1][2],
        "B3": list[1][3],
        "C1": list[2][1],
        "C2": list[2][2],
        "C3": list[2][3]
    }
    while True:
        player_coordinates = (input("choose your coordinates: ").upper())
        if player_coordinates == "QUIT":
            exit()
        elif player_coordinates not in move_dict:
            print("The coordinates were entered in the wrong format")
            continue
        elif move_dict[player_coordinates] == ".":
            return player_coordinates
        else:
            print("This place is taken!")


def menu():
    pass

def wprowadzenie_koordynatow_przez_uzytkownika():
    pass

def init_board(board):
    pass

def podstawienie_znakow(input_uzytkownika):
    pass

def check_win():
    pass

def clear():
    pass

def quit():
    pass

def wprowadzenie_strzału_przez_uzytkownika(): 
    pass