from typing import List

def max_profit(prices: List[int]) -> int:
    l, r = 0, 1
    profit = 0

    while r < len(prices):
        if prices[l] <= prices[r]:
            profit = max(profit, prices[r] - prices[l])
        else:
            l = r
        r += 1

    return profit