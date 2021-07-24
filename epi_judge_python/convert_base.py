from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    char_map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if num_as_string == '0':
        return '0'
    start_idx = 1 if num_as_string.startswith('+') or num_as_string.startswith('-') else 0
    num = 0
    mag = 1
    for c in reversed(num_as_string[start_idx:]):
        num_c = ord(c) - ord('0')
        if num_c > 9:
            num_c = ord(c) - ord('A') + 10
        num += mag * num_c
        mag *= b1
    ret_array = []
    while num > 0:
        ret_array.append(char_map[num % b2])
        num //= b2
    if num_as_string.startswith('-'):
        ret_array.append('-')
    return ''.join(reversed(ret_array))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
