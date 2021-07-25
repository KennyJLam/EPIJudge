from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    cmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ret = 0
    i, i_next = 0, 1
    while i_next < len(s):
        c, c_next = s[i], s[i_next]
        i_num, i_num_next = cmap[c], cmap[c_next]
        if i_num >= i_num_next:
            ret += i_num
            i += 1
            i_next += 1
        else:
            ret += i_num_next - i_num
            i += 2
            i_next += 2
    if i < len(s):
        ret += cmap[s[i]]
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
