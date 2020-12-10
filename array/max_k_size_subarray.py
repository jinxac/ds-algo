"""
https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/
"""

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  start  = 0
  end = 0
  g_res = 0
  res = 0

  while end < len(arr):
    res += arr[end]
    if end >= k - 1:
      g_res = max(res, g_res)
      res -= arr[start]
      start += 1

    end += 1

  return g_res
