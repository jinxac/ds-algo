class Solution:

  def fill_pos(self, arr, count, pos, value):
      while count > 0:
        arr[pos] = value
        pos += 1
        count -= 1

      return pos


  def sort_0_1_2s(self, arr):
    temp = [0, 0, 0]

    for element in arr:
      if element == 0:
        temp[0] += 1
      elif element == 1:
        temp[1] += 1
      else:
        temp[2] += 1

    pos = 0



    # for element in temp:
    next_pos = self.fill_pos(arr, temp[0], 0, 0)
    next_pos = self.fill_pos(arr, temp[1], next_pos, 1)
    next_pos = self.fill_pos(arr, temp[2], next_pos, 2)

if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  solution = Solution()
  solution.sort_0_1_2s(arr)
  print(arr)