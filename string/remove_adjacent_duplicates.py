"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        temp = []
        temp.append(S[0])

        for i in range(1, len(S)):
            element = S[i]
            if temp and temp[-1] == element:
                temp.pop()
            else:
                temp.append(S[i])

        return ''.join(temp)

