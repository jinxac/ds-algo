"""
https://leetcode.com/problems/maximum-product-subarray/
"""

class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        curr_min = arr[0]
        curr_max = arr[0]
        global_max = arr[0]

        for i in range(1, len(arr)):
            m = arr[i] * curr_min
            c = arr[i] * curr_max

            curr_min = min(arr[i], c, m)
            curr_max = max(arr[i], c, m)

            global_max = max(global_max, curr_min, curr_max)

        return global_max
