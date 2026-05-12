class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                width = i - stack[-1] - 1 if stack else i  
                max_area = max(max_area, heights[idx] * width)    
            stack.append(i)

        while stack:
            idx = stack.pop()
            width = len(heights) - stack[-1] - 1 if stack else len(heights)  
            max_area = max(max_area, heights[idx] * width)

        return max_area