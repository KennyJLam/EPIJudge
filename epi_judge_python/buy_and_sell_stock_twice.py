from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    if len(prices) < 2:
        return 0
    best_buy1 = -prices[0]
    best_sell1, best_buy2, best_sell2 = -float('inf'), -float('inf'), 0
    for i in range(1, len(prices)):
        best_sell2 = max(best_sell2, prices[i] + best_buy2)
        best_buy2 = max(best_buy2, -prices[i] + best_sell1)
        best_sell1 = max(best_sell1, prices[i] + best_buy1)
        best_buy1 = max(best_buy1, -prices[i])
    return max(0, max(best_sell1, best_sell2))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
