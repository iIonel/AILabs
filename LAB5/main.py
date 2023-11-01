import copy
from colorama import init, Fore

def print_sudoku(sudoku):
    init(autoreset=True)
    print()
    if sudoku is None:
        print("Invalid")
    else:
        ok = 1
        print('-' * 25)
        for i in range(9):
            if i % 3 == 0 and i > 0:
                print('-' * 25)
            for j in range(9):

                if (j % 3 == 0 and j > 0) or j == 0:
                    print("|", end=" ")

                if len(sudoku[(i, j)]) == 1:
                    if (i, j) in grey_frames:
                        print(Fore.LIGHTGREEN_EX + str(sudoku[(i, j)][0]), end=" ")
                    else:
                        print(sudoku[(i, j)][0], end=" ")
                else:
                    ok = 0
                    if (i, j) in grey_frames:
                        print(Fore.LIGHTGREEN_EX + str(0), end=" ")
                    else:
                        print(0, end=" ")

                if j == 8:
                    print("|", end=" ")
            print()
        print('-' * 25)
        if ok:
            print("Solved")
        print()
        print()

def init_sudoku():
    print("Your Sudoku: ")
    sudoku = {}
    for i in range(9):
        line = input().split()
        for j in range(9):
            element = int(line[j])
            if element == 0:
                sudoku[(i, j)] = list(range(1, 10))
            else:
                sudoku[(i, j)] = [element]
    return sudoku

def init_grey():
    print("Your Grey Frames: ")
    final_list = []
    user_input = input()
    user_input = [int(element) for element in user_input.split()]
    for el in range(0, len(user_input), 2):
        tuple_ = (user_input[el], user_input[el + 1])
        final_list.append(tuple_)
    return final_list

def restriction(sudoku, grey_frames, element, i, j):
    current_row = [sudoku[i, col][0] for col in range(9) if col != j and len(sudoku[(i, col)]) == 1]
    if element in current_row:
        return False

    current_col = [sudoku[(row, j)][0] for row in range(9) if row != i and len(sudoku[(row, j)]) == 1]
    if element in current_col:
        return False

    current_submatrix = [sudoku[(row, col)][0] for row in range(3 * (i // 3), 3 * (i // 3) + 3)
                         for col in range(3 * (j // 3), 3 * (j // 3) + 3) if
                         (row, col) != (i, j) and len(sudoku[(row, col)]) == 1]
    if element in current_submatrix:
        return False

    if (i, j) in grey_frames and element % 2 != 0:
        return False

    return True

def get_empty(sudoku):
    return [(i, j) for i in range(9) for j in range(9) if len(sudoku[(i, j)]) != 1]

def forward_checking(sudoku, i, j, value):
    for col in range(9):
        if col != j and value in sudoku[(i, col)]:
            sudoku[(i, col)].remove(value)

    for row in range(9):
        if row != i and value in sudoku[(row, j)]:
            sudoku[(row, j)].remove(value)

    for row in range(3 * (i // 3), 3 * (i // 3)+ 3):
        for col in range(3 * (j // 3), 3 * (j // 3) + 3):
            if (row, col) != (i, j) and value in sudoku[(row, col)]:
                sudoku[(row, col)].remove(value)

def mrv(emptys, sudoku):
    return min(emptys, key=lambda x: len(sudoku[x]))

def algorithm(sudoku, emptys):
    if not emptys:
        return sudoku

    i, j = mrv(emptys, sudoku)
    for value in sudoku[(i, j)]:
        if restriction(sudoku, grey_frames, value, i, j):
            sudoku_copy = copy.deepcopy(sudoku)
            sudoku_copy[(i, j)] = [value]

            forward_checking(sudoku_copy, i, j, value)

            #print_sudoku(sudoku_copy)
            solve = algorithm(sudoku_copy, get_empty(sudoku_copy))
            if solve is not None:
                return solve

    return None

sudoku = init_sudoku()
grey_frames = init_grey()
emptys = get_empty(sudoku)
print_sudoku(sudoku)
final = algorithm(sudoku, emptys)
print_sudoku(final)