from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    primes = []
    sieve = [True] * n
    sieve[0] = False
    for i in range(1, n + 1):
        if not sieve[i - 1]:
            continue
        primes.append(i)
        j = i * 2
        while j <= n:
            sieve[j - 1] = False
            j += i

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
