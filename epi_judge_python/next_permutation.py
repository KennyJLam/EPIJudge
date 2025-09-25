from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    if len(perm) <= 1:
        return []
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    if i < 0:
        return []
    j = i
    while (j + 1) < len(perm) and (perm[j + 1] > perm[i]) :
        j += 1
    perm[i], perm[j] = perm[j], perm[i]
    for k in range((len(perm) - i - 1) // 2):
        perm[i + k + 1], perm[-(k + 1)] = perm[-(k + 1)], perm[i + k + 1]
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
