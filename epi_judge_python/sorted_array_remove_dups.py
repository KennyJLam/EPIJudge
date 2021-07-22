import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    write_idx = 1
    for read_idx in range(1, len(A)):
        if A[read_idx] != A[read_idx - 1]:
            A[write_idx] = A[read_idx]
            write_idx += 1
    return write_idx


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    # delete_duplicates([2,3,5,5,7,11,11,11,13])
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
