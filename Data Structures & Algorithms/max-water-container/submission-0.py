class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(heights) - 1
        for i in range(len(heights) - 1):
            maxArea = max(maxArea, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea
