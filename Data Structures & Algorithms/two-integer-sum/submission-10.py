class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in twoSum:
                return [twoSum[difference], idx]
            twoSum[num] = idx