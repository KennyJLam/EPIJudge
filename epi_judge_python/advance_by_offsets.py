from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    max_step = 0
    for i in range(len(A)):
        if i > max_step:
            return False
        max_step = max(max_step, i + A[i])
        if max_step >= len(A) - 1:
            return True
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
