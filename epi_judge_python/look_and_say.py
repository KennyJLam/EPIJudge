from test_framework import generic_test


def look_and_say(n: int) -> str:
    cur_array, prev_array = ['1'], []
    for i in range(1, n):
        prev_array, cur_array = cur_array, prev_array
        cur_array.clear()
        num, prev_num, num_count = prev_array[0], prev_array[0], 1
        for j in range(1, len(prev_array)):
            num = prev_array[j]
            if num != prev_num:
                cur_array.append(str(num_count))
                cur_array.append(prev_num)
                prev_num = num
                num_count = 1
            else:
                num_count += 1
        cur_array.append(str(num_count))
        cur_array.append(num)
    return ''.join(cur_array)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
