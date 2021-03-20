from collections import deque

class Solution:
  def solve(self, n, connections):
    matrix = []
    visited = [0] * n

    for i in range(n):
      matrix.append([0] * n)

    for connection in connections:
      x,y = connection
      matrix[x][x] = 1
      matrix[x][y] = 1
      matrix[y][x] = 1
      matrix[y][y] = 1

    dq = deque()

    for i in range(n):
      if visited[i] == 0:
        dq.appendleft(i)
        visited[i] = 1
        dq_size = len(dq)

        for _ in range(dq_size):
          row = dq.pop()
          for j in range(len(matrix[0])):
            if matrix[row][j] == 1 and visited[row] == 0:
              dq.appendleft(j)
              visited[j] == 1
            elif visited[j] == 1:
              return True

    return False
