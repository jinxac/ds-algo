'''
An array contains both positive and negative numbers in random order.

Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples :

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5


Note: Order of elements is not important here.
'''

class Solution:
  def solve(self, arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
      if arr[start] < 0 and arr[end] < 0:
        start += 1
      elif arr[start] > 0 and arr[end] < 0:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end += 1
      elif arr[start] > 0 and arr[end] > 0:
        end -= 1
      else:
        start += 1
        end -= 1

