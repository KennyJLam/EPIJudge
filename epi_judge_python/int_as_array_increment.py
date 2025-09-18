from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    i = len(A) - 1
    while i >= 0:
        A[i] = (A[i] + 1) % 10
        if A[i] != 0:
            break
        i -= 1
    if A[0] == 0:
        # A.insert(0, 1)
        # Clever trick from book.  Finally carry can only happen with all 9's.
        # So final value will always be a power of 10, and current array will always
        # Just be all 0's.  So just set MSD to 1 and append 0 for O(1) operation.
        A.append(0)
        A[0] = 1
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
