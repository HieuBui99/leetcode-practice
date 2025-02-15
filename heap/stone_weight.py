import heapq
from typing import List

def last_stone_weight(stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        x = - stones[0]
        heapq.heappop(stones)
        y = - stones[0]
        heapq.heappop(stones)

        if x == y:
            continue
        elif x > y:
            heapq.heappush(stones, -x + y)
        else:
            heapq.heappush(stones, -y + x)