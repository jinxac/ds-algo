class Solution:
  '''
    This is classical example of dynamic programming.
    The algorithm involved here is called Kadane's algorithm
    and following is how it works:-

    1. Take an index, i, in the array and check its value.
    2. Now individually check sum of  (i, i-1), (i,i-1, i-2) and so on till (i, i-1, i-2, 0)
    3. Take the max value of these sums as well as the individual value in step 1.This max value
    becomes you local/current max
    4. Assign local max to global max if local max is greater than global max
  '''
  def max_sub_array(self, arr):
    if not arr:
      return 0

    global_max = current_max = arr[0]

    for i in range(1, len(arr)):
      current_max = max(current_max + arr[i], arr[i])
      global_max = max(global_max, current_max)

    return global_max


if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  solution = Solution()
  print(solution.max_sub_array(arr))
