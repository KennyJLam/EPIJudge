from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit = 0
    best_px = prices[0]
    for i in range(1, len(prices)):
        price = prices[i]
        max_profit = max(max_profit, price - best_px)
        best_px = min(best_px, price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
