import copy


def read_file(file_path):
    with open(file_path) as f:
        n_generations = f.readline().strip()
        n_generations = int(n_generations)
        width, height = f.readline().strip().split()
        table = f.read().splitlines()
        for i in range(len(table)):
            table[i] = list(table[i])
    return n_generations, width, height, table


# j - cols, i - rows
def next_cell(table, row, col):
    c = 0
    cond = table[row][col]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not ((i == 0) and (j == 0)):
                ind_i = (row + i) % len(table)
                ind_j = (col + j) % len(table[0])
                if table[ind_i][ind_j] == "x":
                    c+=1
    if table[row][col] == "." and c == 3:
        cond = "x"
    elif table[row][col] == "x" and not (c == 2 or c == 3):
        cond = "."

    return cond


def next_generation(table):
    copied_table = copy.deepcopy(table)
    for i in range(len(table)):
        for j in range(len(table[0])):
            copied_table[i][j] = next_cell(table,i,j)

    return copied_table


def gen_generation(table,n_generations):
    for i in range(n_generations):
        table = next_generation(table)

    return table


def print_result(table):
    for i in table:
        print("".join(i))