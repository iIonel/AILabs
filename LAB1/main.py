#EX1
import time
init =  [1, 2, 3, 4, 5, 8, 6, 7, 0]
#my_matrix = init_matrix(init) -> transpunerea informatiilor pe o matrice de 3x3


#EX2
def is_final(st):
    contor = 1
    for i in range(3):
        for j in range(3):
            if st[i][j] != 0 and st[i][j] != contor:
                return 0
            elif st[i][j] != 0 and st[i][j] == contor:
                contor = contor + 1
    return 1

def init_probl(st):
    matrix = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(0, len(init)):
        matrix[i // 3][i % 3] = init[i]
    return matrix


#EX3
#direction = -1 -> LEFT
#direction = 1 -> RIGHT
#direction = -2 -> DOWN
#direction = 2 -> UP

def search_zero(st):
    for i in range(3):
        for j in range(3):
            if st[i][j] == 0:
                return [i,j]

def validate_position(st, direction, position):
    if direction == -1 and 0 <= position[1] - 1 < 3:
        st[position[0]][position[1]], st[position[0]][position[1] - 1] = st[position[0]][position[1] - 1], st[position[0]][position[1]]
        position[1] -= 1
        return 1
    elif direction == 1 and 0 <= position[1] + 1 < 3:
        st[position[0]][position[1]], st[position[0]][position[1] + 1] = st[position[0]][position[1] + 1], st[position[0]][position[1]]
        position[1] += 1
        return 1
    elif direction == -2 and 0 <= position[0] + 1 < 3:
        st[position[0]][position[1]], st[position[0] + 1][position[1]] = st[position[0] + 1][position[1]], st[position[0]][position[1]]
        position[0] += 1
        return 1
    elif direction == 2 and 0 <= position[0] - 1 < 3:
        st[position[0]][position[1]], st[position[0] - 1][position[1]] = st[position[0] - 1][position[1]], st[position[0]][position[1]]
        position[0] -= 1
        return 1
    else:
        return 0

def move(st, direction, position):
    validate_position(st,direction,position)
    return st

def print_matrix(st):
    for i in range(3):
        for j in range(3):
            print(st[i][j], end=" ")
        print()
    print()


#----------------------------------------------------#
#EX4
def iddfs(st, position, max_depth):
    for depth in range(max_depth):
        if dfs(st, position, depth) == 1:
            return 1
    return 0

def dfs(st, position, depth):
    if depth == 0:
        return 0
    if is_final(st):
        return 1
    for dir in [-1, 1, -2, 2]:
        copy_st = [row[:] for row in st]
        copy_pos = position.copy()
        if validate_position(copy_st, dir, copy_pos):
            dfs_result = dfs(copy_st, copy_pos, depth - 1)
            if dfs_result == 1:
                return 1
    return 0

st = init_probl(init)
print_matrix(st)
initial_position = search_zero(st)

start = time.time()
solution = iddfs(st, initial_position, max_depth=30)
end = time.time()

if solution == 1:
    print("Great!")
else:
    print("No solution!")

elapsed_time = (end - start)
print(f"Elapsed Time: {elapsed_time:.6f} seconds")