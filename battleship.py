from tabulate import tabulate
import copy
import os


def changing_table(player, player_move, list):
    if len(player_move) == 2:
        row = int(player_move[1])
        column = letter_to_number(player_move[0])
        list[column][row] = player
        return list

def letter_to_number(letter):
    letters_to_numbers = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
    }
    return letters_to_numbers.get(letter)

def print_table(list):
    head = [" ", "1", "2", "3", "4", "5"]
    return(tabulate(list, headers=head, tablefmt="fancy_grid"))

print(print_table([["A", 0, 0, 0, 0, 0], ["B", 0, 0, 0, 0, 0], ["C", 0, 0, 0, 0, 0], ["D", 0, 0, 0, 0, 0], ["E", 0, 0, 0, 0, 0]]))


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

def stawianie_statkow_na_planszy():
    pass

def init_board():
    board = [["A", x, 0, 0, 0, 0], ["B", 0, 0, x, 0, 0], ["C", 0, 0, 0, 0, 0], ["D", 0, 0, x, 0, 0], ["E", 0, 0, 0, 0, 0]]
    return board


def has_won(board):
    if board.count("S") == 6:
        print("Player1 has one!!!")
        exit()
    else:
        return None

def podstawienie_znakow_X(input_uzytkownika):
    pass

def podstawienie_znakow_innych():
    pass

def check_win():
    pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit(user_input):   #w menu 
    if user_input.lower() == 'quit':
        print('Thanks for playing. Good Bye')
        menu()


def zatapianie_statkow(): 
    pass

def delay():
    pass

def get_move(board, player):     
    row, col = 3, 3     
    possible_moves = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]     
    move = input("WHERE YOU WANT TO SHOOT?: ")      
    if move.lower() == "quit":         
        close_game()     
    elif move.lower() not in possible_moves:         
        print("TRY TO HIT THE BOARD!!!")         
        return get_move(board,player)   
    if "a" in move.lower():         
        row = 0     
    elif "b" in move.lower():        
        row = 1     
    elif "c" in move.lower():         
        row = 2     
    if board[row][col] != 0:         
        print("THIS SPOT IS TAKEN. TRY TO HIT ANOTHER ONE!!!")         
        return get_move(board, player)     
    return row, col

def game_logic():
    board = init_board()
    print_table(board)
    user1_input = stawianie_statkow_na_planszy()
    podstawienie_znakow_X(user1_input)
    print_table(board)
    delay()
    board2 = init_board()
    print_table(board2)
    user2_input = stawianie_statkow_na_planszy()
    podstawienie_znakow_X(user2_input)
    print_table(board2)
    board3 = init_board()
    board4 = init_board()
    while True:
        print_table(board3 + board4)
        user1_input = zatapianie_statkow()
        podstawienie_znakow_innych(board3, user1_input)
        has_won()
        print_table(board3 + board4)
        user2_input = zatapianie_statkow()
        podstawienie_znakow_innych(board4, user2_input)
        has_won()
