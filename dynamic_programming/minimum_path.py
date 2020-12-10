"""
https://leetcode.com/problems/minimum-path-sum/
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [None] * len(grid)

        for i in range(len(dp)):
            dp[i] = [0] * len(grid[0])

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]

                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]

                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[len(grid) - 1][len(grid[0]) - 1]