"""
https://leetcode.com/contest/weekly-contest-218/problems/max-number-of-k-sum-pairs/
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = collections.Counter()
        res = 0

        for element in nums:
            if k - element in counter:
                res += 1
                counter[k-element] -= 1
                if counter[k-element] == 0:
                    del counter[k-element]
            else:
                counter[element] += 1

        return res
