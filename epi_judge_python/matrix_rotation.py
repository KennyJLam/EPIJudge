from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    n = len(square_matrix)
    sub_n = n
    while sub_n > 1:
        offset = (n - sub_n) // 2
        for i in range(sub_n - 1):
            (square_matrix[offset][i + offset], square_matrix[i + offset][n - offset - 1],
             square_matrix[n - offset - 1][n - offset - 1 - i], square_matrix[n - offset - 1 - i][offset]) \
                = (square_matrix[n - offset - 1 - i][offset], square_matrix[offset][i + offset], square_matrix[i + offset][n - offset - 1],
                   square_matrix[n - offset - 1][n - offset - 1 - i])
        sub_n -= 2
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
