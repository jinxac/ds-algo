"""
https://leetcode.com/problems/shuffle-string/
"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = []
        for i in range(len(s)):
            temp.append([s[i], indices[i]])

        res = [""] * len(s)


        for element in temp:
            res[element[1]] = element[0]

        return ''.join(res)