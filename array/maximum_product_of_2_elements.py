"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
"""

import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hq = heapq.nlargest(2, nums)
        return (hq[0]-1) * (hq[1]-1)
