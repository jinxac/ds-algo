class Solution():
  def solve(self, arr):
    self.res = []

    def merge(arr, start, end):
      if end - start > 1:
        return

      print("start...", start, end)

      x1 = arr[start][0]
      x2 = arr[start][1]

      y1 = arr[end][0]
      y2 = arr[end][1]


      if x1 <= y1 <= x2 <= y2:
        self.res.append([x1, y2])

      elif y1 <= x1 <= y2 <= x2:
        self.res.append([y1, x2])

      else:
        self.res.append(arr[start])
        self.res.append(arr[end])


    def traverse(arr, start, end):
      if start < end:
        mid = (start + end) // 2
        traverse(arr, start, mid)
        traverse(arr, mid + 1 , end)
        merge(arr, start, end)

    traverse(arr, 0, len(arr) - 1)
    return self.res

if __name__ == "__main__":
  # arr = [int(x) for x in input().split()]
  arr = [[1,2],[3,4],[1,6]]
  s = Solution()
  print(s.solve(arr))
  # print(arr)