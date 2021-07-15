from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    i = len(A) - 1
    carry = True
    while i >= 0 and carry:
        A[i] = (A[i] + 1) % 10
        carry = A[i] == 0
        i -= 1
    if carry:
        A[0] = 1
        A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
