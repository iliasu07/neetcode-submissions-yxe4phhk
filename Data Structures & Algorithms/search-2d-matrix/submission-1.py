class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            left, right = 0, len(mat) - 1
            if target > mat[right]:
                continue
            elif target == mat[right]:
                return True
            else:
                while left <= right:
                    mid = (left + right) // 2
                    if target < mat[mid]:
                        right = mid - 1
                    elif target > mat[mid]:
                        left = mid + 1
                    else:
                        return True
        return False
