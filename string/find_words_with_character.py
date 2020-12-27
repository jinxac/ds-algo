"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
"""

from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        temp = Counter(chars)
        res = 0

        for word in words:
            can_form = True
            temp_sub = Counter(word)
            for key, value in temp_sub.items():
                if not temp[key] >= value:
                    can_form = False

            if can_form:
                res += len(word)

        return res