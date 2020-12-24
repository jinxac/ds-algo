"""
https://leetcode.com/problems/number-of-islands/
"""

class Solution:
    def traverse(self, grid, i, j):
        if i < 0 or i > len(grid) - 1:
            return

        if j < 0 or j >  len(grid[0]) - 1:
            return

        if grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.traverse(grid, i- 1, j)
        self.traverse(grid, i + 1, j)
        self.traverse(grid, i, j - 1)
        self.traverse(grid, i, j + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    answer += 1
                    self.traverse(grid, i, j)

        return answer