"""
https://leetcode.com/problems/palindromic-substrings/
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [None] * len(s)
        res = 0
        cnt = 0

        for i in range(len(dp)):
            dp[i] = [False] * len(dp)


        for gap in range(len(s)):
            column = gap
            row = 0
            while column < len(dp):
                if gap == 0:
                    dp[row][column] = True

                elif gap == 1:
                    if s[row] == s[column]:
                        dp[row][column] = True
                else:
                    if s[row] == s[column] and dp[row+1][column-1]:
                        dp[row][column] = True

                if dp[row][column]:
                    cnt += 1

                row += 1
                column += 1

        return cnt