from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def linked_list_len(L: ListNode) -> int:
    if L is None:
        return 0
    h = L
    lln = 1
    while h.next:
        h = h.next
        lln += 1
    return lln


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return None
    if k == 0:
        return L
    nhead = L
    lln = 1
    k_bigger = False
    for _ in range(k):
        if nhead.next:
            nhead = nhead.next
            lln += 1
        else:
            k_bigger = True
            break
    if k_bigger:
        nhead = L
        mk = k % lln
        if mk == 0:
            return L
        for _ in range(mk):
            if nhead.next:
                nhead = nhead.next
            else:
                nhead = L
    if nhead is L:
        return L
    ntail = L
    while nhead.next:
        ntail = ntail.next
        nhead = nhead.next
    C = ntail.next
    ntail.next = None
    nhead.next = L
    return C


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
