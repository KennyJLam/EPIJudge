from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    sh = sum([ord(c) for c in s])
    th = sum([ord(c) for c in t[:len(s)]])
    for i in range(len(t) - len(s) + 1):
        if i > 0:
            th -= ord(t[i - 1])
            th += ord(t[i + len(s) - 1])
        if sh == th:
            if t[i:i + len(s)] == s:
                return i
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
