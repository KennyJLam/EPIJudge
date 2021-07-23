from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    prev = -1
    maxed = True
    for i in reversed(range(len(perm))):
        if perm[i] < prev:
            maxed = False
            break
        prev = perm[i]
    if maxed:
        return []
    pos = perm[i]
    for j in reversed(range(len(perm))):
        if pos < perm[j]:
            break
    ret = perm[:i]
    ret.append(perm[j])
    stub = perm[i + 1:]
    stub[j - i - 1] = perm[i]
    ret.extend(reversed(stub))
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
