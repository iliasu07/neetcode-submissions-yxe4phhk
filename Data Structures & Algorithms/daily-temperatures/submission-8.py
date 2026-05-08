class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        # temperatures = [30,38,30,36,35,40,28]
        # result = [1, 0, 0, 0, 0, 0, 0]
        # stack = [1, 2]
        # i = 2
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop() 
                result[idx] = i - idx
            stack.append(i)
                
        return result
