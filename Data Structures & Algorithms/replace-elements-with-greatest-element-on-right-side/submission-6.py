class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_arr = []
        for idx in range(len(arr)):
            max_arr = arr[idx+1::]
            if max_arr:
                arr[idx] = max(max_arr)
        
        arr[-1] = -1

        return arr