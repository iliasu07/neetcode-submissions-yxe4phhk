# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []
        return self.mergeSortSolver(pairs, 0, len(pairs)-1)


    def mergeSortSolver(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs

        middle = (start + end) // 2

        self.mergeSortSolver(pairs, start, middle)
        self.mergeSortSolver(pairs, middle + 1, end)
        self.merge(pairs, start, middle, end)

        return pairs


    def merge(self, pairs, start, middle, end):
        leftPair = pairs[start : middle+1]
        rightPair = pairs[middle+1 : end+1]

        lPointer = 0
        rPointer = 0
        pPointer = start
        
        while lPointer < len(leftPair) and rPointer < len(rightPair):
            if leftPair[lPointer].key <= rightPair[rPointer].key:
                pairs[pPointer] = leftPair[lPointer]
                lPointer += 1
                
            else:
                pairs[pPointer] = rightPair[rPointer]
                rPointer += 1
            pPointer += 1

        while lPointer < len(leftPair):
            pairs[pPointer] = leftPair[lPointer]
            lPointer += 1
            pPointer += 1

        while rPointer < len(rightPair):
            pairs[pPointer] = rightPair[rPointer]
            rPointer += 1
            pPointer += 1


        
