from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    goal = len(A) - 1
    reach = 0
    for i in range(len(A)):
        if i > reach:
            return False
        reach = max(reach, i + A[i])
        if reach >= goal:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
