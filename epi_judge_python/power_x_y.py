from test_framework import generic_test


def power(x: float, y: int) -> float:
    ret_val = 1
    pos_y = abs(y)
    while pos_y != 0:
        pow_bit = pos_y & ~(pos_y - 1) # get first set bit
        pos_y &= pos_y - 1 # clear first set bit
        x_pow = x
        pow_bit >>= 1
        while pow_bit != 0:
            x_pow *= x_pow
            pow_bit >>= 1
        ret_val *= x_pow
    if y < 0:
        ret_val = 1 / ret_val
    return ret_val


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
