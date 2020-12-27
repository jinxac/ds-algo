"""
https://leetcode.com/problems/richest-customer-wealth/
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = -1
        for account in accounts:
            temp = 0
            for i in range(len(account)):
                temp += account[i]

            res = max(res, temp)

        return res
