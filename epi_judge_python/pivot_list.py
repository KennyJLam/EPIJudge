import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    if not l:
        return None
    lt_head, eq_head, gt_head = ListNode(), ListNode(), ListNode()
    lt_tail, eq_tail, gt_tail = lt_head, eq_head, gt_head
    cursor = l
    while cursor:
        if cursor.data < x:
            lt_tail.next = cursor
            lt_tail = cursor
        elif cursor.data == x:
            eq_tail.next = cursor
            eq_tail = cursor
        else:
            gt_tail.next = cursor
            gt_tail = cursor
        cursor = cursor.next
    ret = lt_head.next if lt_head.next else eq_head.next if eq_head.next else gt_head.next
    if lt_head.next:
        lt_tail.next = eq_head.next if eq_head.next else gt_head.next if gt_head.next else None
    if eq_head.next:
        eq_tail.next = gt_head.next if gt_head.next else None
    gt_tail.next = None
    return ret


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
