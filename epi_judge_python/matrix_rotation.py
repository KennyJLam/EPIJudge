from typing import List

from test_framework import generic_test


def rotate_ring(matrix: List[List[int]], start_idx, sq_len) -> None:
    for i in range(sq_len - 1):
        cx, cy = start_idx, start_idx + i
        buffer = matrix[cx][cy]

        cx, cy = cy, len(matrix) - start_idx - 1
        buffer, matrix[cx][cy] = matrix[cx][cy], buffer

        cx, cy = len(matrix) - start_idx - 1, len(matrix) - cx - 1
        buffer, matrix[cx][cy] = matrix[cx][cy], buffer

        cx, cy = cy, start_idx
        buffer, matrix[cx][cy] = matrix[cx][cy], buffer

        cx, cy = start_idx, start_idx + i
        matrix[cx][cy] = buffer
    return


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    sq_len = len(square_matrix)
    for i in range(len(square_matrix) // 2):
        rotate_ring(square_matrix, i, sq_len)
        sq_len -= 2
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
