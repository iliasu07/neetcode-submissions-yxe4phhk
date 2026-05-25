from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))     

    def get(self, key: str, timestamp: int) -> str:
        res = -1
        pairs = self.m[key]
        left, right = 0, len(pairs) - 1

        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        return "" if res == -1 else pairs[res][1] 