from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if start == 0:
        return L
    dhead = ListNode()
    dhead.next = L
    idx = 1
    n_insert = dhead
    while idx < start:
        n_insert = n_insert.next
        if n_insert is None:
            return L
        idx += 1
    n_terminal = n_insert
    while idx <= finish:
        n_terminal = n_terminal.next
        idx += 1
    n_remove = n_insert.next
    while n_insert.next != n_terminal:
        n_swap = n_remove.next
        n_remove.next = n_swap.next
        n_swap.next = n_insert.next
        n_insert.next = n_swap
    return dhead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
