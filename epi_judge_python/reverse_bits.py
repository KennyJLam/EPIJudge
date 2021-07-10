from test_framework import generic_test

swap_cache = [0b0000, 0b1000, 0b0100, 0b1100,
              0b0010, 0b1010, 0b0110, 0b1110,
              0b0001, 0b1001, 0b0101, 0b1101,
              0b0011, 0b1011, 0b0111, 0b1111]


def reverse_bits(x: int) -> int:
    ret_val = 0
    mask = 0b1111
    for i in range(16):
        ret_val <<= 4
        ret_val |= swap_cache[x & mask]
        x >>= 4
    return ret_val


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
