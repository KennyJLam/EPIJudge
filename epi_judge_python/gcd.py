from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    x, y = abs(x), abs(y)
    if x == 0:
        return y
    if y == 0:
        return x
    if x == 1 or y == 1:
        return 1
    two_factor = 0
    while x & 1 == 0 and y & 1 == 0:
        x >>= 1
        y >>= 1
        two_factor += 1
    while x & 1 == 0:
        x >>= 1
    while y & 1 == 0:
        y >>= 1
    while x != y:
        if x < y:
            x, y = y, x
        x = x - y
        if x & 1 == 0:
            x >>= 1
    return x << two_factor


if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.py', 'gcd.tsv', gcd))
