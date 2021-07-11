from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    if x & 1 == 0:
        fbit = x & ~(x - 1)
        return (x ^ fbit) | (fbit >> 1) # move first 1 bit to the right
    else:
        fbit = (x + 1) & ~x
        return x ^ (fbit | (fbit >> 1)) # swap first 0 bit with the right


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
