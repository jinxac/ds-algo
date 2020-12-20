"""
https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return None
        start = 0
        rows = len(matrix)
        columns = len(matrix[0])
        end = rows * columns - 1

        while start <= end:
            mid = (start + end) // 2
            num = matrix[mid // columns][mid % columns]
            if num == target:
                return True

            if num > target:
                end = mid - 1
            else:
                start = mid + 1

        return False


