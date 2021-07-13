from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    if x == 0:
        return True
    if x < 0:
        return False;
    upper_mask = 10**int(math.log10(x))
    lower_mask = 1
    while upper_mask > lower_mask:
        if (x // upper_mask) % 10 != (x // lower_mask) % 10:
            return False
        upper_mask //= 10
        lower_mask *= 10
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
