from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    if L1.data <= L2.data:
        head, L1 = L1, L1.next
    else:
        head, L2 = L2, L2.next
    tail = head
    while L1 is not None or L2 is not None:
        if L1 is None:
            tail.next = L2
            break
        if L2 is None:
            tail.next = L1
            break
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
