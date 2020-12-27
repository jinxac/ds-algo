"""
https://leetcode.com/problems/is-subsequence/
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        start = 0
        s_start = 0

        while start < len(t):
            if s_start < len(s) and s[s_start] == t[start]:
                s_start += 1

            start += 1

        return s_start == len(s)