class Solution:
    def solve(self, n):
        if n == 1:
            return 1

        return n * self.solve(n-1)

    def dp_solve(self, n):
        dp = [1] * (n+1)

        for i in range(2,n+1):
            dp[i] = i * dp[i-1]

        print(dp)
        return dp[n]

    def bare_array(self, n):
      arr = [1]

      for current_num in range(2, n+1):
        carry = 0
        pos = 0
        while pos < len(arr):
          temp = arr[pos] * current_num + carry
          carry, temp = divmod(temp, 10)
          arr[pos] = temp
          pos += 1

        while carry:
          carry, val = divmod(carry, 10)
          arr.append(val)

      arr = list(reversed(arr))
      for i in range(len(arr)):
        arr[i] = str(arr[i])

      return ''.join(arr)





    """
      n * (n-1) * (n-2) * .... 1
    """
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        s = Solution()
        print(s.bare_array(n))
        t -= 1
