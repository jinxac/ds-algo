class Solution:
  def spiral_matrix(self, arr):
    '''
      left = 0, right = len(row) - 1, top = 0, bottom = len(arr) - 1
      direction = 0, 1, 2, 3
    '''
    res = []
    left = 0

    if not arr:
        return []

    right = len(arr[0]) - 1
    top = 0
    bottom = len(arr) - 1


    direction = 0


    while left <= right and top <= bottom:
        if direction == 0:
            for i in range(left, right+1):
                res.append(arr[top][i])

            top += 1
            direction = 1


        elif direction == 1:
            for i in range(top, bottom + 1):
                res.append(arr[i][right])

            right -= 1
            direction = 2

        elif direction == 2:
            for i in reversed(range(left, right + 1)):
                res.append(arr[bottom][i])

            bottom -= 1
            direction = 3


        elif direction == 3:
            for i in reversed(range(top, bottom + 1)):
                res.append(arr[i][left])

            left += 1
            direction = 0

    return res

if __name__ == "__main__":
  r = int(input("Enter number of rows"))
  c = int(input("Enter number of columns"))

  matrix = []

  for i in range(r):
    row = [int(x) for x in input().split()]
    matrix.append(row)

  solution = Solution()
  solution.spiral_matrix(matrix)
