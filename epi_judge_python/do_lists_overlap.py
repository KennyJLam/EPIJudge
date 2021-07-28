import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    if l0 is None or l1 is None:
        return None
    is_cycle0 = True
    if not l0.next or not l0.next.next:
        is_cycle0 = False
    else:
        slow0, fast0 = l0.next, l0.next.next
        while slow0 is not fast0:
            if not fast0.next or not fast0.next.next:
                is_cycle0 = False
                break
            slow0 = slow0.next
            fast0 = fast0.next.next

    is_cycle1 = True
    if not l1.next or not l1.next.next:
         is_cycle1 = False
    else:
        slow1, fast1 = l1.next, l1.next.next
        while slow1 is not fast1:
            if not fast1.next or not fast1.next.next:
                is_cycle1 = False
                break
            slow1 = slow1.next
            fast1 = fast1.next.next

    if is_cycle0 and not is_cycle1:
        return None
    elif not is_cycle0 and is_cycle1:
        return None
    elif is_cycle0 and is_cycle1:
        fast0 = slow0.next
        cycle0_len = 1
        is_intersect = fast0 is slow1
        while fast0 is not slow0:
            fast0 = fast0.next
            cycle0_len += 1
            if fast0 is slow1:
                is_intersect = True
        if not is_intersect:
            return None
        slow0, fast0 = l0, l0
        for _ in range(cycle0_len):
            fast0 = fast0.next
        while fast0 is not slow0:
            slow0 = slow0.next
            fast0 = fast0.next
        return slow0
    else:
        len0 = 1
        node = l0
        while node.next:
            len0 += 1
            node = node.next
        len1 = 1
        node = l1
        while node.next:
            len1 += 1
            node = node.next
        diff = abs(len0 - len1)
        if len0 >= len1:
            n0, n1 = l0, l1
        else:
            n0, n1 = l1, l0
        for _ in range(diff):
            n0 = n0.next
        while n0 is not n1:
            n0 = n0.next
            n1 = n1.next
        return n0



@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
