class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicates = defaultdict(int)
        for num in nums:
            if num in hasDuplicates:
                return True
            hasDuplicates[num] = 1
        return False
