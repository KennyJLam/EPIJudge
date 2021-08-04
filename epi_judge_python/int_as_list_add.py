from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    if not L1 or not L2:
        return None
    lsum = ListNode()
    ltail = lsum
    carry = 0
    d1, d2 = L1, L2
    while d1 or d2 or carry:
        a1 = d1.data if d1 else 0
        a2 = d2.data if d2 else 0
        sum = a1 + a2 + carry
        nd = sum % 10
        ltail.next = ListNode(data=nd)
        ltail = ltail.next
        carry = sum // 10
        if d1:
            d1 = d1.next
        if d2:
            d2 = d2.next
    return lsum.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
