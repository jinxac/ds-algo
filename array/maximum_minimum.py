import sys

class Solution:
  def get_max_min(self, arr):
    max_element = -sys.maxsize - 1
    min_element = sys.maxsize

    for element in arr:
      min_element = min(min_element, element)
      max_element = max(max_element, element)

    print(max_element, min_element)


if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  solution = Solution()
  solution.get_max_min(arr)
