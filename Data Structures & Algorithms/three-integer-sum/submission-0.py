class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for idx, num in enumerate(nums):
            if num > 0:
                break

            if idx > 0 and num == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1
            while left < right:
                if num + nums[left] + nums[right] > 0:
                    right -= 1
                elif num + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return result