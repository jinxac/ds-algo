"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3567/
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        start = 0
        end = len(nums) - 1
        high_index = len(nums) - 1

        while start <= end:
            left_sq = nums[start] ** 2
            right_sq = nums[end] ** 2

            if right_sq > left_sq:
                result[high_index] = right_sq
                end -= 1
            else:
                result[high_index] = left_sq
                start += 1

            high_index -= 1

        return result