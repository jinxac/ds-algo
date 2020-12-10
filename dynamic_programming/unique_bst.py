class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, len(dp)):
            dp[i] = dp[1] * dp[i-1] * 2
            for j in range(1, i - 1):
                dp[i] += dp[j] * dp[i-j - 1]

        return dp[n]