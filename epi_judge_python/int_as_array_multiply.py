from typing import List

from test_framework import generic_test

# Add nums2 into num1
def add(num1, num2, pow):
    carry = 0
    for i in range(len(num2)):
        dsum = num2[i] + num1[i] + carry
        num1[i] = dsum % 10
        carry = 1 if dsum >= 10 else 0
    i = len(num2)
    while carry == 1 and i < len(num1):
        carry = 1 if num1[i] == 9 else 0
        num1[i] = (num1[i] + 1) % 10
        i += 1
    if carry == 1:
        num1.append(1)


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    num1, num2 = list(reversed(num1)), list(reversed(num2))

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
