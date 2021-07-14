import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    r1_left, r1_right, r1_top, r1_bottom = r1.x, r1.x + r1.width, r1.y + r1.height, r1.y
    r2_left, r2_right, r2_top, r2_bottom = r2.x, r2.x + r2.width, r2.y + r2.height, r2.y
    if r1_left <= r2_right and r1_right >= r2_left and r1_top >= r2_bottom and r1_bottom <= r2_top:
        int_left = max(r1_left, r2_left)
        int_right = min(r1_right, r2_right)
        int_top = min(r1_top, r2_top)
        int_bottom = max(r1_bottom, r2_bottom)
        return Rect(int_left, int_bottom, int_right - int_left, int_top - int_bottom)
    else:
        return Rect(0, 0, -1, -1)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
