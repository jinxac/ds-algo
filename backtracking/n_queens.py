class Solution:
  def is_under_attack(self, matrix, row, column):
    if row < 0 or row > len(matrix) - 1:
      return False

    if column < 0 or column > len(matrix) - 1:
      return False

    for i in range(row, len(matrix)):
      if 1 in matrix[i]:
        return False

    for i in range(column, len(matrix[0])):
      if 1 in list(zip(*matrix[i])):
        return False


    i = row
    j = column

    while i <= row and j <= column:
      if matrix[i][j] == 1:
        return False

      i += 1
      j += 1

    i = len(matrix)
    j = len(matrix[0])

    while i >= row and j >= column:
      if matrix[i][j] == 1:
        return False

      i -= 1
      j -= 1

    return True


  def n_queen_place(self, matrix, n):
    if n == 0:
      return True

    i = 0
    j = 0

    while i < len(matrix):
      while j < len(matrix[0]):
        if self.is_under_attack(matrix, i, j):
          continue

        matrix[i][j] = 1
        if self.n_queen_place(matrix, n-1):
          return True

        matrix[i][j] = 0

    return False



  def solve(self, matrix, n):
    return self.n_queen_place(matrix, n)
