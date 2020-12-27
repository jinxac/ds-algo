"""
https://leetcode.com/problems/matrix-diagonal-sum/
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0

        left = 0
        top = 0
        right = len(mat[0]) - 1
        bottom = 0

        while top < len(mat) and left < len(mat[0]) and right >= 0 and bottom < len(mat[0]):
            s += mat[top][left]
            s += mat[bottom][right]

            if left == right:
                s -= mat[top][left]
            bottom += 1
            right -= 1
            top += 1
            left += 1


        return s
