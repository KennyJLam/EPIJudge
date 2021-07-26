from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    ret = []
    for i in range(1, min(4, len(s) - 2)):
        if int(s[:i]) > 255 or (s[0] == '0' and i > 1):
            break
        for j in range(i + 1, min(i + 4, len(s) - 1)):
            if int(s[i:j]) > 255 or (s[i] == '0' and j > i + 1):
                break
            for k in range(j + 1, min(j + 4, len(s))):
                if int(s[j:k]) > 255 or (s[j] == '0' and k > j + 1):
                    break
                if int(s[k:]) <= 255 and not (s[k] == '0' and k < len(s) - 1):
                    ret.append('.'.join([s[:i], s[i:j], s[j:k], s[k:]]))
    return ret


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
