from test_framework import generic_test


def divide(x: int, y: int) -> int:
    divisor = 0
    exp = 1
    while y < x:
        y <<= 1
        exp <<= 1

    while y > 0:
        while y > x:
            y >>= 1
            exp >>= 1
        divisor += exp
        x -= y

    return divisor


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
