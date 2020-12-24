"""
https://leetcode.com/problems/rotting-oranges/
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = -1

        # initial start position as string
        start_pos = '00'
        one_count = 0
        dq = deque()

        # calculating number of 2s and 1s
        # appending 2s to the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    start_pos = str(i) + str(j)
                    dq.append(start_pos)
                if grid[i][j] == 1:
                    one_count += 1

        # if there are no 2s present, check for 1s
        # if no 1s return 0 else -1
        if not dq:
            if one_count:
                return -1
            return 0


        # bfs search, check for top, left, right, bottom
        while dq:
            dq_size = len(dq)
            for _ in range(dq_size):
                element = dq.pop()
                # split element to get x, y coordinate
                x, y = [int(x) for x in element]

                # if element is 2, check for adjacent cell 1s
                # Make 1s to 2s and append to queue
                # Decrement 1s count for each 1 encountered

                if grid[x][y] == 2:
                    if x> 0 and grid[x-1][y] == 1:
                        one_count -= 1
                        grid[x-1][y] = 2
                        dq.appendleft(str(x-1) + str(y))
                    if x+1 < len(grid) and grid[x+1][y] == 1:
                        one_count -= 1
                        grid[x+1][y] = 2
                        dq.appendleft(str(x+1) + str(y))
                    if y > 0 and grid[x][y-1] == 1:
                        one_count -= 1
                        grid[x][y-1] = 2
                        dq.appendleft(str(x) + str(y-1))
                    if y+1 < len(grid[0]) and grid[x][y+1] == 1:
                        one_count -= 1
                        grid[x][y+1] = 2
                        dq.appendleft(str(x) + str(y+1))

            res += 1

        # if 1st exist return -1
        if one_count > 0:
            return -1
        return res

