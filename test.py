import pytest

from utils import read_file, next_cell, next_generation


@pytest.fixture(scope='function')
def fill_test_file():
    with open('input.txt', 'w') as w:
        w.write(
            "5\n"
            "8 5\n"
            "...x....\n"
            "....x...\n"
            "..xxx...\n"
            "........\n"
            "........\n"
        )

def read_file_test(fill_test_file):
    n_generations, width, height, table = read_file('input.txt')
    assert n_generations == 3
