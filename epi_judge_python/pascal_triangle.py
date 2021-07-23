from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n == 0:
        return []
    ret = [[1]]
    for i in range(1, n):
        ret.append([1])
        for j in range(1, i):
            ret[i].append(ret[i - 1][j - 1] + ret[i - 1][j])
        ret[i].append(1)
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
