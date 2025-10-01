from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    out = []
    for i in range(n):
        out.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                out[i].append(1)
            else:
                out[i].append(out[i - 1][-j] + out[i - 1][-j - 1])
    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
