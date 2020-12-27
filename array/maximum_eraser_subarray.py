"""
https://leetcode.com/problems/maximum-erasure-value/
"""

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        curr_sum = 0
        max_sum = -math.inf
        temp = {}

        while end < len(nums):
            while nums[end] in temp:
                curr_sum -= nums[start]
                temp[nums[start]] -= 1
                if temp[nums[start]] == 0:
                    del temp[nums[start]]
                start += 1

            curr_sum += nums[end]
            max_sum = max(curr_sum, max_sum)

            if not nums[end] in temp:
                temp[nums[end]] = 0
            temp[nums[end]] += 1

            end += 1

        max_sum = max(curr_sum, max_sum)

        return max_sum