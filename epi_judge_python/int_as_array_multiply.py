from typing import List
from test_framework import generic_test


def reverse_digits(num):
    i, j = 0, len(num) - 1
    while i < j:
        temp = num[i]
        num[i] = num[j]
        num[j] = temp
        i += 1
        j -= 1


# scale up magnitude ofr num1 than add to num2 and write results into num2.
def add(num1: List[int], num2: List[int], multiplier: int):
    i, j = 0, multiplier
    num1_len = len(num1)
    carry = 0
    while i < num1_len or carry != 0:
        while j >= len(num2):
            num2.append(0)
        digit_sum = num2[j] + (num1[i] if i < num1_len else 0) + carry
        num2[j] = digit_sum % 10
        carry = digit_sum // 10
        i += 1
        j += 1


def mult_single_digit(num1: List[int], num2: int) -> List[int]:
    if num2 == 0:
        return [0]
    result = []
    carry = 0
    for digit in num1:
        prod = digit * num2 + carry
        result.append(prod % 10)
        carry = prod // 10
    if carry != 0:
        result.append(carry)
    return result


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    rnum1, rnum2 = num1.copy(), num2.copy()
    rnum1[0], rnum2[0] = abs(rnum1[0]), abs(rnum2[0])
    reverse_digits(rnum1)
    reverse_digits(rnum2)
    if len(rnum1) < len(rnum2):
        temp = rnum1
        rnum1 = rnum2
        rnum2 = temp
    is_neg = (num1[0] < 0) ^ (num2[0] < 0)

    result = []
    i = 0
    while i < len(rnum2):
        digit2 = rnum2[i]
        single_prod = mult_single_digit(rnum1, digit2)
        add(single_prod, result, i)
        i += 1

    reverse_digits(result)
    if is_neg:
        result[0] *= -1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('int_as_array_multiply.py', 'int_as_array_multiply.tsv', multiply))
