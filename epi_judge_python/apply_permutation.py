from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        if perm[i] < 0:
            continue
        j = i
        buffer = A[j]
        dest = perm[j]
        while dest != i:
            temp = A[dest]
            A[dest] = buffer
            buffer = temp
            perm[j] = -1 * (perm[j] + 1)
            j = dest
            dest = perm[j]
        A[i] = buffer
        perm[j] = -1 * (perm[j] + 1)
    for i in range(len(perm)):
        perm[i] = -1 * (perm[i] - 1)
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
