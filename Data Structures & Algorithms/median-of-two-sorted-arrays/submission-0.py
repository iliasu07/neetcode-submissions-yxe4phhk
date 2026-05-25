class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left, right = 0, 0
        nums = []
        length = len(nums1) + len(nums2)
        for i in range(length):
            if left < len(nums1) and right < len(nums2) and nums1[left] <= nums2[right]:
                nums.append(nums1[left])
                left += 1

            elif left < len(nums1) and right < len(nums2) and nums1[left] > nums2[right]:
                nums.append(nums2[right])
                right += 1

            else:
                if left == len(nums1):
                    nums.append(nums2[right])
                    right += 1
                else:
                    nums.append(nums1[left])
                    left += 1
        #[1,2,3,4,5,6]
        if length % 2 == 1:
            median = nums[length // 2]
        else:
            median = (nums[length // 2 - 1] + nums[length // 2]) / 2

        return median
