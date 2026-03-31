class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force
        #max_arr = []
        #for idx in range(len(arr)):
        #    max_arr = arr[idx+1::]
        #    if max_arr:
        #        arr[idx] = max(max_arr)
        #
        #arr[-1] = -1

        #return arr

        N = len(arr)
        new_arr = [0] * N
        rightMax = -1

        for idx in range(N-1, -1, -1):
            new_arr[idx] = rightMax
            rightMax = max(arr[idx], rightMax)
        
        return new_arr
    