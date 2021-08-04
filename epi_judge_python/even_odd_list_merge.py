from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return None
    if not L.next:
        return L
    ehead, etail = L, L
    ohead, otail = L.next, L.next
    cursor = L.next.next
    bit = 0
    while cursor:
        if bit:
            otail.next = cursor
            otail = otail.next
        else:
            etail.next = cursor
            etail = etail.next
        cursor = cursor.next
        bit ^= 1
    etail.next = ohead
    otail.next = None
    return ehead


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
