"""
https://leetcode.com/problems/max-increase-to-keep-city-skyline
"""

class Solution:
    def pythonic_way(self, grid):
        top = list(map(max,grid))
        left = list(map(max, zip(*grid)))

        actual_sum = sum(map(sum, grid))
        final_sum = sum(min(i,j) for i in top for j in left)
        print(actual_sum, final_sum)


        return final_sum - actual_sum

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        return self.pythonic_way(grid)
        top = []
        left = []
        res = 0

        for row in range(len(grid)):
            top.append(max(grid[row]))

        for column in zip(*grid):
            left.append(max(column))

        for i in range(len(grid)):
            for j in range(len(grid)):
                res = res + (min(top[i], left[j]) - grid[i][j])

        return res
