class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        N = len(temperatures)
        # temperatures = [30,38,30,36,35,40,28]
        for i in range(N):
            count = 1
            j = i+1
            while j < N:
                if temperatures[i] < temperatures[j]:
                    break
                else:
                    j += 1 
                    count += 1 
            count = 0 if j == N else count
            result.append(count)

        return result
