from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True
    if not L.next:
        return True
    if not L.next.next:
        return L.data == L.next.data
    # get mid-point of list
    slow, fast = L, L
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # reverse second half of list
    rhead = slow
    rtail = slow.next
    while rtail.next:
        temp = rhead.next
        rhead.next = rtail.next
        rtail.next = rtail.next.next
        rhead.next.next = temp
    # compare two halves
    cursor, rcursor = L, rhead.next
    ret = True
    while rcursor:
        if cursor.data != rcursor.data:
            ret = False
            break
        cursor = cursor.next
        rcursor = rcursor.next
    # unreverse second half of list
    fhead, ftail = slow, slow.next
    while ftail.next:
        temp = fhead.next
        fhead.next = ftail.next
        ftail.next = ftail.next.next
        fhead.next.next = temp
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
