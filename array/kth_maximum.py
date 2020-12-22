import heapq

class Solution:
  def get_kth_max(self, arr, k):
    return heapq.nlargest(k, arr)[-1]

  def get_kth_min(self, arr, k):
    return heapq.nsmallest(k, arr)[-1]

if __name__ == "__main__":
  k = int(input())
  arr = [int(x) for x in input().split()]
  solution = Solution()
  print(solution.get_kth_max(arr, k))
  print(solution.get_kth_min(arr, k))2