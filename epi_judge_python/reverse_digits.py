from test_framework import generic_test


def reverse(x: int) -> int:
    rev_x = 0
    is_neg = x < 0
    x = abs(x)
    while x > 0:
        rev_x *= 10
        rev_x += x % 10
        x //= 10
    return rev_x * (-1 if is_neg else 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
