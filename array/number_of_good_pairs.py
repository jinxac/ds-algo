"""
https://leetcode.com/problems/number-of-good-pairs/
"""

from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dp = [1] * 100
        dp[1] = 0
        dp[2] = 1

        for i in range(3,len(dp)):
            dp[i] = (i-1) + dp[i-1]

        temp = dict(Counter(nums))

        res = 0
        for val in temp.values():
            res += dp[val]

        return res