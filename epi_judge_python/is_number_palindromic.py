from test_framework import generic_test
import math

# First try
# def is_palindrome_number(x: int) -> bool:
#     if x < 0:
#         return False
#     if x == 0:
#         return True
#     n_digits = math.floor(math.log10(x)) + 1
#     for i in range(n_digits // 2):
#         j = n_digits - i - 1
#         if ((x // 10**i) % 10) != ((x // 10**j) % 10):
#             return False
#     return True

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    n_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (n_digits - 1)
    for _ in range(n_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
