from typing import List
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    
    a, b = 1, 2        
    for i in range(3, n+1):
        res = a + b
        a = b
        b = res
    return res


def min_cost_clime_stairs(cost: List[int]) -> int:
    cache = [0] * len(cost)
    cache[1] = 0

    for i in range(2, len(cost)):
        cache[i] = min(cache[i-1] + cost[i-1], cache[i-2] + cost[i-2])
    n = len(cost)
    return min(cache[n-1] + cost[n-1], cache[n-2] + cost[n-2])


