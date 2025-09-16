from test_framework import generic_test


def power(x: float, y: int) -> float:
    y_resid = abs(y)
    ans = 1
    while y_resid > 0:
        factor = x
        exp = 1
        tracker = y_resid >> 1
        while tracker > 0:
            factor *= factor
            exp <<= 1
            tracker >>= 1
        ans *= factor
        y_resid -= exp

    return ans if y > 0 else 1 / ans


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
