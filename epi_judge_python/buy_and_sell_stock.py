from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    if len(prices) < 2:
        return 0
    min_price = -prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] + min_price)
        min_price = max(min_price, -prices[i])
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
