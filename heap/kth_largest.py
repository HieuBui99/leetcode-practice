import heapq
from typing import List

def kth_largest(k: int, nums: List[int]) -> int:
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, nums[i])
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]