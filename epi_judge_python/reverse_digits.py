from test_framework import generic_test
import math


def reverse(x: int) -> int:
    ret_val = 0
    pos_x = abs(x)
    while pos_x > 0:
        ret_val *= 10
        ret_val += pos_x % 10
        pos_x //= 10
    if x < 0:
        ret_val *= -1
    return ret_val


def reverse_by_swap(x: int) -> int: # this turns out to be slower
    ret_val = 0
    pos_x = abs(x)
    top_bit = int(math.log10(pos_x))
    bottom_bit = 0
    while top_bit >= bottom_bit:
        top_digit = pos_x // int(10**top_bit) % 10
        bottom_digit = pos_x // int(10**bottom_bit) % 10
        ret_val += top_digit * 10**bottom_bit
        if top_bit != bottom_bit:
            ret_val += bottom_digit * 10**top_bit
        top_bit -= 1
        bottom_bit += 1
    if x < 0:
        ret_val *= -1
    return ret_val


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
