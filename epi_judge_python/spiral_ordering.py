from typing import List

from test_framework import generic_test


def spiral_iter(matrix: List[List[int]], start_r, start_c, m_len) -> List[int]:
    if m_len == 1:
        return [matrix[start_r][start_c]]
    ret = []
    for i in range(m_len):
        ret.append(matrix[start_r][start_c + i])
    for i in range(1, m_len):
        ret.append(matrix[start_r + i][start_c + m_len - 1])
    for i in reversed(range(m_len - 1)):
        ret.append(matrix[start_r + m_len - 1][start_c + i])
    for i in reversed(range(1, m_len - 1)):
        ret.append(matrix[start_r + i][start_c])
    return ret


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    m_len = len(square_matrix)
    start_r, start_c = 0, 0
    ret = []
    while m_len > 0:
        ret.extend(spiral_iter(square_matrix, start_r, start_c, m_len))
        m_len -= 2
        start_r += 1
        start_c += 1
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
