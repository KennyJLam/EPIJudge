from typing import List

from test_framework import generic_test
import math


# Given n, return all primes up to and including n.
# Trial division method
# def generate_primes(n: int) -> List[int]:
#     if n <= 1:
#         return []
#     primes = [2]
#     current = 3
#     while current <= n:
#         cap = int(math.sqrt(current)) + 1
#         for prime in primes[1:]:
#             if prime > cap:
#                 primes.append(current)
#                 break
#             if current % prime == 0:
#                 break
#         else:
#             primes.append(current)
#         current += 2
#
#     return primes

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    if n <= 1:
        return []
    primes = [2]
    num_candidates = (n - 3) // 2 + 1
    candidates = [True] * num_candidates
    for i in range(num_candidates):
        prime = 2*i + 3
        if candidates[i]:
            primes.append(prime)
        for j in range(2*i**2 + 6*i + 3, num_candidates, prime):
            candidates[j] = False

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
