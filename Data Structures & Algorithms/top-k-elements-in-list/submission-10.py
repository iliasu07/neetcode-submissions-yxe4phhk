class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        output = []
        for i in range(k):
            output.append(sorted_frequency[i][0])
        return output