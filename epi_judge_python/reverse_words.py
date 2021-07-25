import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reverse_sub(s, start_idx: int, end_idx: int):
    i, j = start_idx, end_idx - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    if len(s) == 0:
        return
    reverse_sub(s, 0, len(s))
    start_idx, end_idx = 0, 0
    while end_idx < len(s):
        while not s[start_idx].isalnum():
            start_idx += 1
            if start_idx >= len(s):
                return
        end_idx = start_idx
        while end_idx < len(s) and s[end_idx].isalnum():
            end_idx += 1
        reverse_sub(s, start_idx, end_idx)
        start_idx = end_idx
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
