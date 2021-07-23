from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    for i in range(9):
        row_s = set()
        col_s = set()
        big_s = set()
        big_row = i // 3
        big_col = i % 3
        for j in range(9):
            if partial_assignment[i][j] != 0:
                if partial_assignment[i][j] in row_s:
                    return False
                row_s.add(partial_assignment[i][j])
            if partial_assignment[j][i] != 0:
                if partial_assignment[j][i] in col_s:
                    return False
                col_s.add(partial_assignment[j][i])
            big_cell = partial_assignment[big_row * 3 + j // 3][big_col * 3 + j % 3]
            if big_cell != 0:
                if big_cell in big_s:
                    return False
                big_s.add(big_cell)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
