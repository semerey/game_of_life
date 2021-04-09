from utils import *


def run_game():

    file_test = "..\\game_of_life\\input_data.txt"
    n_generations, width, height, table = read_file(file_test)

    print_result(gen_generation(table, n_generations))