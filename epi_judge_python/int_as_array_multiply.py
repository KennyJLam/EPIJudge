from typing import List

from test_framework import generic_test



def multiply(num1: List[int], num2: List[int]) -> List[int]:
    n, m = len(num1), len(num2)
    prod = [0]*(n + m)
    sign_mult = 1
    if num1[0] < 0:
        num1[0] *= -1
        sign_mult *= -1
    if num2[0] < 0:
        num2[0] *= -1
        sign_mult *= -1
    for i in range(m - 1, -1, -1):
        mult = num2[i]
        carry = 0
        prod_idx = None
        for j in range(n - 1, -1, -1):
            dp = mult * num1[j]
            prod_idx = n + m - (m - i - 1) - (n - j - 1) - 1
            prod[prod_idx] +=  dp + carry
            carry = prod[prod_idx] // 10
            prod[prod_idx] %= 10
        while carry > 0:
            prod_idx -= 1
            prod[prod_idx] += carry
            carry = prod[prod_idx] // 10
            prod[prod_idx] %= 10
    zero_idx = 0
    while zero_idx < len(prod) and prod[zero_idx] == 0:
        zero_idx += 1
    if zero_idx == len(prod):
        prod = prod[-1:]
    else:
        prod = prod[zero_idx:]
    prod[0] *= sign_mult
    return prod


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
