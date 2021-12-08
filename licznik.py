board = [["A", 0, 0, 0, 0, 0], ["B", 0, 's', 0, 0, 0], ["C", 0, 0, 's', 0, 0], ["D", 0, 0, 0, 's', 0], ["E", 0, 0, 0, 0, 0]]

def counter_s(board):
    counter = 0
    for i in range(len(board)):
        number = board[i].count('s')     
        counter += number
    return counter
    

def check_win(counter):  
    if counter == 6:
        return True
    else:
        return False
       
counter_s(board)