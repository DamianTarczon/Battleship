from tabulate import tabulate


def print_table(list1, list2):
    head = [" ", "1", "2", "3", "4", "5", " ", " ", "1", "2", "3", "4", "5"]
    print_arr = []
    for index, _ in enumerate(list1):
        row = list1[index] + [" "] + list2[index]
        print_arr.append(row)
    
    print(tabulate(print_arr, head , tablefmt="fancy_grid"))


board = [["A", 0, 0, 0, 0, 0], ["B", 0, 's', 0, 0, 0], ["C", 0, 0, 's', 0, 0], ["D", 0, 0, 0, 's', 0], ["E", 0, 0, 0, 0, 0]]
board2 = [["A", 'x', 3, 3, 3, 3], ["B", 0, 's', 3, 0, 0], ["C", 0, 0, 's', 0, 0], ["D", 0, 3, 3, 's', 0], ["E", 0, 0, 0, 0, 0]]

print_table(board, board2)
