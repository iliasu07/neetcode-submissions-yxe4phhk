class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,2,3,3,3], k = 2

        topK = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            topK[num] += 1  # {'1':1, '2':2, '3':3}

        for key, value in topK.items():
            bucket[value].append(key)   #[[], [1], [2], [3], [], []]

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res