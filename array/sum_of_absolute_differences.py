"""
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
"""

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_arr = [0] * len(nums)
        right_arr = [0] * len(nums)
        result = 0

        res = [0] * len(nums)

        for i in reversed(range(1, len(nums))):
            right_arr[i-1] = right_arr[i] + nums[i]

        for i in range(1, len(nums)):
            left_arr[i] = left_arr[i-1] + nums[i-1]

        for i in range(len(left_arr)):
            diff = len(left_arr) - i - 1
            if left_arr[i]:
                res[i] +=  abs(left_arr[i] - nums[i] * i)
            if right_arr[i]:
                res[i] += abs(right_arr[i] - nums[i] * diff)

        return res

