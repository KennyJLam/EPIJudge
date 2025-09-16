from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    if x & 1 == 0:
        return x ^ ((x & ~(x - 1)) | ((x & ~(x - 1)) >> 1))
    else:
        return x ^ ((~x & ~(~x - 1)) | ((~x & ~(~x - 1)) >> 1))
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
