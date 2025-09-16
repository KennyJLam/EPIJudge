from test_framework import generic_test

def add(x: int, y: int) -> int:
    ret_sum, carry = x, y
    while carry:
        ret_sum, carry = ret_sum ^ carry, (ret_sum & carry) << 1

    return ret_sum

def multiply(x: int, y: int) -> int:
    ret_prod = 0
    addend, residual = x, y
    while residual:
        if residual & 1:
            ret_prod = add(ret_prod, addend)
        residual >>= 1
        addend <<= 1
    return ret_prod


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
