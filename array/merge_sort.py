class Solution():
  def solve(self, arr):
    def merge(start, mid, end):
      temp = []

      i = start
      j = mid + 1

      while i <= mid and j <= end:
        if arr[i] < arr[j]:
          temp.append(arr[i])
          i += 1
        else:
          temp.append(arr[j])
          j += 1

      while i <= mid:
        temp.append(arr[i])
        i += 1

      while j <= end:
        temp.append(arr[j])
        j += 1

      for i in range(len(temp)):
        arr[i+start] = temp[i]


    def merge_sort(start, end):
      if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        merge(start, mid, end)

    merge_sort(0, len(arr) - 1)


if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  s = Solution()
  s.solve(arr)
  print(arr)
