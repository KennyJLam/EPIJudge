from test_framework import generic_test

# Less Efficient
# def swap_bits(x, i, j):
#     if i == j:
#         return x
#     if i > j:
#         i, j = j, i
#     x ^= (x & (1 << i)) << (j - i)
#     x ^= (x & (1 << j)) >> (j - i)
#     x ^= (x & (1 << i)) << (j - i)
#
#     return x

def swap_bits(x, i, j):
    if ((x >> i) & 1) ^ ((x >> j) & 1) == 0:
        return x
    x ^= (1 << i) | (1 << j)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
