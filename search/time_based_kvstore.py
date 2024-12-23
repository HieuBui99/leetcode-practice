
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.hash_map[key]) == 0: 
            return ""

        arr = self.hash_map[key]
        
        res = ""
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            prev_timestamp = arr[mid][1]
            if prev_timestamp > timestamp:
                r = mid - 1
            else:
                res = arr[mid][0]
                l = mid + 1
        return res