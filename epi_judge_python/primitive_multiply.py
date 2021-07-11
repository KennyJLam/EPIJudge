from test_framework import generic_test


def add(x: int, y: int) -> int:
    ret_sum = 0
    carry_bit = 0
    add_mag = 1
    while x != 0 or y != 0 or carry_bit == 1:
        next_bit = (x & 1) ^ (y & 1) ^ carry_bit
        if next_bit == 1:
            ret_sum |= add_mag
        carry_bit = ((x & 1) & (y & 1)) | ((x & 1) & carry_bit) | ((y & 1) & carry_bit)
        x >>= 1
        y >>= 1
        add_mag <<= 1
    return ret_sum


def multiply(x: int, y: int) -> int:
    ret_prod = 0
    while y != 0:
        if y & 1 == 1:
            ret_prod = add(x, ret_prod)
        x <<= 1
        y >>= 1
    return ret_prod


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
