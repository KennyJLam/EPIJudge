from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    n = len(square_matrix)
    n_iter = n
    i, j = 0, -1
    spiral_mat = []
    while n_iter > 0:
        if n_iter == 1:
            j += 1
            spiral_mat.append(square_matrix[i][j])
            break
        for _ in range(n_iter):
            j += 1
            spiral_mat.append(square_matrix[i][j])
        for _ in range(n_iter - 1):
            i += 1
            spiral_mat.append(square_matrix[i][j])
        for _ in range(n_iter - 1):
            j -= 1
            spiral_mat.append(square_matrix[i][j])
        for _ in range(n_iter - 2):
            i -= 1
            spiral_mat.append(square_matrix[i][j])
        n_iter -= 2
    return spiral_mat


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
