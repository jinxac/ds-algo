"""
https://leetcode.com/problems/spiral-matrix-ii/
"""

import numpy as np

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []

        for i in range(n):
            res.append([0] * n)


        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        direction = 0
        cnt = 1


        while left <= right and top <= bottom:
            if direction == 0:
                for i in range(left, right+1):
                    res[top][i] = cnt
                    cnt += 1

                top += 1
                direction = 1

            elif direction == 1:
                for i in range(top, bottom+1):
                    res[i][right] = cnt
                    cnt += 1

                right -= 1
                direction = 2

            elif direction == 2:
                for i in reversed(range(left, right+1)):
                    # res.append(cnt)
                    res[bottom][i] = cnt
                    cnt += 1

                bottom -= 1
                direction = 3

            elif direction == 3:
                for i in reversed(range(top, bottom+1)):
                    # res.append(cnt)
                    res[i][left] = cnt
                    cnt += 1

                left += 1
                direction = 0


        return res


