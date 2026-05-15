class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1 
        maxLeft, maxRight = 0, 0
        water = 0
        i = 0
        while left < right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            if maxLeft > maxRight:
                water += maxRight - height[right]
                right -= 1
            else:
                water += maxLeft - height[left]
                left += 1

            i += 1
        return water
                