"""
Rearrange array in alternating positive & negative items with O(1) extra space | Set 1
Given an array of positive and negative numbers, arrange them in an alternate fashion such
that every positive number is followed by negative and vice-versa maintaining the order of appearance.
Number of positive and negative numbers need not be equal. If there are
more positive numbers they appear at the end of the array.
If there are more negative numbers, they too appear in the end of the array.

Examples :

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

"""

class Solution:
  def stack_approach(self, arr):
    p_stack = []
    n_stack = []
    res = []

    for element in arr:
      if element < 0:
        n_stack.append(element)
      else:
        p_stack.append(element)

    i = 0
    j = 0

    while i < len(p_stack) and j < len(n_stack):
      res.append(n_stack[j])
      res.append(p_stack[i])
      i += 1
      j += 1

    while i < len(p_stack):
      res.append(p_stack[i])
      i += 1

    while j < len(n_stack):
      res.append(n_stack[j])
      j += 1

    return res

  def solve(self, arr):
    return self.stack_approach(arr)



if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  solution = Solution()
  res = solution.solve(arr)
  print(res)
