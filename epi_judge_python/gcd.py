from test_framework import generic_test


# my solution (faster)
def gcd_a(x: int, y: int) -> int:
    if x == y:
        return x
    a, b = min(x, y), max(x, y)
    if a == 0:
        return b
    if a == 1:
        return 1
    while a != b:
        a, b = min(a, b), max(a,b)
        grow = a
        next_grow = a << 1
        while next_grow < b:
            grow = next_grow
            next_grow <<= 1
        b -= grow
    return a


# book solution
def gcd_b(x: int, y: int) -> int:
    if x == y:
        return x
    a, b = min(x, y), max(x, y)
    if a == 0:
        return b
    if a == 1:
        return 1
    mult = 0
    while a != b:
        a, b = min(a, b), max(a,b)
        if not (a & 1) and not (b & 1):
            mult += 1
            a >>= 1
            b >>= 1
        elif not a & 1:
            a >>= 1
        elif not b & 1:
            b >>= 1
        else:
            b -= a
    return a << mult


def gcd(x: int, y: int) -> int:
    return gcd_b(x, y)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.py', 'gcd.tsv', gcd))
