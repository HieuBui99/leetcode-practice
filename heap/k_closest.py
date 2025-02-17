import math
import heapq
from typing import List

def distance(point1: List[int], point2: List[int]) -> float:
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


#min heap solution
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for point in points:
        dist = distance(point, [0, 0])
        heap.append([dist, point])
    heapq.heapify(heap)

    res = []
    while k > 0:
        dist, point = heap[0]
        heapq.heappop(heap)
        res.append(point)
        k -= 1
    return res


#max heap solution
def kClosest2(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for point in points:
        dist = - distance(point, [0, 0])
        heapq.heappush(heap, [dist, point])
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    while heap:
        _, point = heap[0]
        res.append(point)
        heapq.heappop(heap)

    return res