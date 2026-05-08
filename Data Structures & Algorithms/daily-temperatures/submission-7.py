class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        N = len(temperatures)
        for i in range(N):
            j = i+1
            while j < N:
                if temperatures[i] < temperatures[j]:
                    result.append(j-i)
                    break
                j += 1 
            else:
                result.append(0)

        return result
