from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dhead = ListNode(next=L)
    tail = dhead
    for _ in range(k):
        tail = tail.next
    head = dhead
    while tail.next:
        head = head.next
        tail = tail.next
    head.next = head.next.next
    return dhead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
