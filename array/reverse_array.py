class Solution:
  def reverse_integer(self, arr):
    i = 0
    j = len(arr) - 1

    while i < j:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j -= 1

  def reverse_python(self, arr):
    arr.reverse()

  def reverse_python_slice(self, arr):
    '''
      Python slice function has following syntax arr[start:end:step]
      To reverse we keep step as -1 and avoid start and end
    '''
    reversed_arr = arr[::-1]

if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  solution = Solution()
  solution.reverse_integer(arr)
  print(arr)