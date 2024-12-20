import math
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    res = r

    while l <= r:
        mid = (l + r) // 2

        t = sum([math.ceil(x / mid) for x in piles])

        if t <= h:
            res = mid
            r = mid - 1
        else:
            l = mid + 1

    return res