from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_profit1 = 0
    max_profit1_cache = []
    best_px1 = prices[0]
    for i in range(len(prices)):
        price = prices[i]
        max_profit1 = max(max_profit1, price - best_px1)
        max_profit1_cache.append(max_profit1)
        best_px1 = min(best_px1, price)

    max_profit = max_profit1
    best_px2 = prices[-1]
    for i in reversed(range(1, len(prices))):
        price = prices[i]
        max_profit = max(max_profit, best_px2 - price + max_profit1_cache[i - 1])
        best_px2 = max(best_px2, price)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
