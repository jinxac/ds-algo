class Solution:

    def binary_search_optimized(self, arr, n, m):
      global_cnt = 0
      res = 0
      i = 0

      while i < n:
        if i == 0:
          cnt = 0
          start = 0
          end = m - 1
          start_pos = -1

          while start <= end:
            mid = (start + end) // 2
            if (mid == 0 or arr[i][mid - 1] == 0) and arr[i][mid] == 1:
              start_pos = mid
              break

            if arr[i][mid] == 0:
              start = mid + 1
            else:
              end = mid - 1

          if start_pos != -1:
            cnt = m - start_pos

          if cnt > global_cnt:
            global_cnt = cnt
            res = i

        elif arr[i][m - global_cnt - 1]  == 1:
          while global_cnt < m and arr[i][m - global_cnt - 1] != 0:
            global_cnt += 1
          # global_cnt = global_cnt + 1
          res = i

        # if global_cnt == m:
        #   res = i
        #   break
        print("cnt...", global_cnt)
        i += 1

      return res

    def binary_approach(self, arr, n, m):
      global_cnt = 0
      res = -1

      for i in range(n):
        cnt = 0
        start = 0
        end = m - 1
        start_pos = -1

        while start <= end:
          mid = (start + end) // 2
          if (mid == 0 or arr[i][mid - 1] == 0) and arr[i][mid] == 1:
            start_pos = mid
            break

          if arr[i][mid] == 0:
            start = mid + 1
          else:
            end = mid - 1

        if start_pos != -1:
          cnt = m - start_pos

        if cnt > global_cnt:
          global_cnt = cnt
          res = i

      return res

    def rowWithMax1s(self,arr, n, m):
      return self.binary_search_optimized(arr,n, m)


if __name__ == "__main__":
  t = int(input())

  while t > 0:
    n, m = list(map(int, input().strip().split()))

    input_line = list(map(int, input().strip().split()))
    arr = [[0 for j in range(m)] for i in range(n)]


    for i in range(n):
      for j in range(m):
        arr[i][j] = input_line[i * m + j]

    ob = Solution()
    ans = ob.rowWithMax1s(arr, n, m)
    print(ans)
    t -= 1