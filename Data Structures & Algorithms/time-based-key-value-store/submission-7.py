from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(lambda: [[], []])
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key][0].append(value)
        self.time_map[key][1].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.time_map[key][1]) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            
            if self.time_map[key][1][mid] <= timestamp:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return self.time_map[key][0][res] if res != -1 else ""