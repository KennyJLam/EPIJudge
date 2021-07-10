from test_framework import generic_test


def swap_bits(x, i, j):
    mask = 1 << i | 1 << j
    bits = x & mask
    if bits == 0 or bits == mask:
        return x
    return x % mask


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
