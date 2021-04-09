# read input
file_test = "C:\\Users\\Anna\\PycharmProjects\\game_of_life\\input_data.txt"


def read_file(file_path):
    with open(file_path) as f:
        n_generations = f.readline().strip()
        width, height = f.readline().strip().split()
        table = f.read().splitlines()
        for i in table:
            i = list(i)
            print(i)

    return n_generations, width, height, table
n_generations, width, height, table = read_file(file_test)

# j - cols, i - rows
def return_next(table, row, col):
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


