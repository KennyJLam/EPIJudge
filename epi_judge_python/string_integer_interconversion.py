from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if x == 0:
        return '0'
    s = []
    px = abs(x)
    while px > 0:
        s.append(chars[px % 10])
        px //= 10
    if x < 0:
        s.append('-')
    return ''.join(reversed(s))


def string_to_int(s: str) -> int:
    ret = 0
    mag = 1
    start_idx = 1 if s[0] == '-' or s[0] == '+' else 0
    for c in reversed(s[start_idx:]):
        ret += (ord(c) - ord('0')) * mag
        mag *= 10
    if s[0] == '-':
        ret *= -1
    return ret


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
