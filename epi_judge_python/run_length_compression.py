from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    ret = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j].isnumeric():
            j += 1
        for k in range(int(s[i:j])):
            ret.append(s[j])
        i = j + 1
    return ''.join(ret)


def encoding(s: str) -> str:
    ret = []
    count = 0
    for i in range(len(s)):
        count += 1
        if i == len(s) - 1 or s[i + 1] != s[i]:
            ret.append(str(count))
            ret.append(s[i])
            count = 0
    return ''.join(ret)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
