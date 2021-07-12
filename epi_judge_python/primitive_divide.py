from test_framework import generic_test


def divide(x: int, y: int) -> int:
    quotient = 0
    while x >= y:
        up_divisor, divisor = y << 1, y
        qbit = 1
        while up_divisor <= x:
            divisor = up_divisor
            up_divisor <<= 1
            qbit <<= 1
        quotient |= qbit
        x -= divisor
    return quotient


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
