class Solution:
    def recursive_approach(self, n):
        if n <= 3:
            return n

        count = n
        start = 1

        while start * start <= n:
            count = min(count, self.recursive_approach(n - (start * start)) + 1)
            start += 1

        return count

    def bottom_up_approach(self, n):
        dp = [n] * (n+1)

        if n <=3:
            return n
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n+1):
            start = 1
            while start * start <= n:
                dp[i] = min(dp[i], dp[i - start * start] + 1)
                start += 1

        return dp[len(dp) - 1]



    def numSquares(self, n: int) -> int:
        return self.bottom_up_approach(n)