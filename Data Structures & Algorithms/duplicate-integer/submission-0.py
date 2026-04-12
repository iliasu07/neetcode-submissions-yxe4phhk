class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}

        for n in nums:
            if n in duplicate:
                return True
            else:
                duplicate[n] = 1
        return False  