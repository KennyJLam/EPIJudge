from test_framework import generic_test


def parity(x: int) -> int:
    return log_parity(x)


# obvious solution
def bit_by_bit_parity(x: int) -> int:
    p = 0
    while x > 0:
        p ^= x & 1
        x >>= 1
    return p


def log_parity(x: int) -> int:
    shrink = (x >> 32) ^ (x & 0xffffffff)
    shrink = (x >> 16) ^ (x & 0xffff)
    shrink = (x >> 8) ^ (x & 0xff)
    return bit_by_bit_parity(shrink)


if __name__ == '__main__':
    print('running...')
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
