from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    ret = 0
    mag = 1
    for c in reversed(col):
        ret += mag * (ord(c) - ord('A') + 1)
        mag *= 26
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
