"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        temp = {'a': 1, 'e': 1, 'i': 1, 'o':1, 'u': 1}
        left_count = 0
        right_count = 0

        mid = len(s) // 2

        for i in range(0, mid):
            if s[i].lower() in temp:
                left_count += 1

        for i in range(mid, len(s)):
            if s[i].lower() in temp:
                right_count += 1

        return left_count == right_count

