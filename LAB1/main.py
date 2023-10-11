#EX1
init =  [8, 6, 7, 2, 5, 4, 0, 3, 1]
matrix = [[0 for _ in range(3)] for _ in range(3)]
for i in range(0, len(init)):
    matrix[i % 3][i//3] = init[i]

print(matrix)


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
        matrix[i % 3][i // 3] = init[i]
    return matrix

st_init = init
is_final(init) #?


#EX3