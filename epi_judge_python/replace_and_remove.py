import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    cur_len = size
    write_c = 0
    num_adds = 0
    for i in range(cur_len):
        if s[i] == 'a':
            num_adds += 1
        if s[i] != 'b':
            s[write_c] = s[i]
            write_c += 1
    del_len = write_c
    new_len = write_c + num_adds
    write_c = new_len - 1
    for i in reversed(range(del_len)):
        if s[i] == 'a':
            s[write_c] = 'd'
            write_c -= 1
            s[write_c] = 'd'
            write_c -= 1
        else:
            s[write_c] = s[i]
            write_c -= 1
    return new_len


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
