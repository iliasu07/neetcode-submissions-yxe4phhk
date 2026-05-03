class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in position:
                return [position[complement], idx]

            position[num] = idx