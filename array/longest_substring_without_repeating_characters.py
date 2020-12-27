"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

import math

class Solution:
    def sliding_way(self, s):
        start = 0
        end = 0
        res = -math.inf
        temp = {}

        while end < len(s):
            while s[end] in temp:
                temp[s[start]] -= 1
                if temp[s[start]] == 0:
                    del temp[s[start]]

                start += 1

            if not s[end] in temp:
                temp[s[end]] = 0

            temp[s[end]] += 1

            res = max(res, end - start + 1)
            end += 1

        if res == -math.inf:
            return 0

        return res



    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.sliding_way(s)

