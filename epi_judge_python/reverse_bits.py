from test_framework import generic_test


def reverse_bits(x: int) -> int:
    for i in range(32):
        if ((x >> i) & 1) != ((x >> (63 - i)) & 1):
            x ^= (1 << i) | (1 << (63 - i))
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
