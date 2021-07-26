import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: Optional[ListNode], l1: Optional[ListNode]) -> Optional[ListNode]:
    if l0 is None or l1 is None:
        return None
    head0, len0 = l0, 1
    while head0.next:
        len0 += 1
        head0 = head0.next
    head1, len1 = l1, 1
    while head1.next:
        len1 += 1
        head1 = head1.next
    diff = abs(len0 - len1)
    big_head = l0 if len0 >= len1 else l1
    for i in range(diff):
        big_head = big_head.next
    head0, head1 = (big_head, l1) if len0 >= len1 else (l0, big_head)
    while head0 is not head1:
        if not head0.next or not head1.next:
            return None
        head0 = head0.next
        head1 = head1.next
    return head0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
