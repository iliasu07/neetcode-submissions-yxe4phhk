class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        # sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
# 
        # output = []
        # for i in range(k):
        #     output.append(sorted_frequency[i][0])


        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in frequency.items():
            bucket[val].append(key)

        output = []
        for idx in range(len(bucket) - 1, 0, -1):
            for num in bucket[idx]:
                output.append(num)
                if len(output) == k:
                    return output

        