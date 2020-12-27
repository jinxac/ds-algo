"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/
"""

from collections import Counter

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        temp = Counter(allowed)
        for word in words:
            start = 0
            should_add = True
            while start < len(word):
                if not word[start] in temp:
                    should_add = False
                    break
                start += 1

            if should_add:
                res += 1


        return res