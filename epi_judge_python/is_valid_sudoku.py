from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    for i in range(9):
        row_nums = set()
        col_nums = set()
        sq_nums = set()
        for j in range(9):
            if partial_assignment[i][j] != 0:
                if partial_assignment[i][j] in row_nums:
                    return False
                row_nums.add(partial_assignment[i][j])
            if partial_assignment[j][i] != 0:
                if partial_assignment[j][i] in col_nums:
                    return False
                col_nums.add(partial_assignment[j][i])
            i_sq = (i // 3) * 3 + j // 3
            j_sq = (i % 3) * 3 + j % 3
            if partial_assignment[i_sq][j_sq] != 0:
                if partial_assignment[i_sq][j_sq] in sq_nums:
                    return False
                sq_nums.add(partial_assignment[i_sq][j_sq])

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
