class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = {}
        for num in nums:
            if num in output:
                return True
            output[num] = 1

        return False