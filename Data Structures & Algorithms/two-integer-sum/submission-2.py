class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in twoSum:
                return [twoSum[diff], idx]
            twoSum[num] = idx

