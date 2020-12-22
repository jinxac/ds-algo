"""
https://leetcode.com/problems/house-robber-ii/
"""

class Solution:

    def parse(self,nums, start, end):
        dp = [0] * len(nums)
        dp[start] = nums[start]


        dp[start + 1] = max(nums[start], nums[start + 1])

        if len(nums) == 2:
            return dp[start + 1]

        for i in range(start + 2, len(nums) - end):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp_first = self.parse(nums, 0, 1)
        dp_second = self.parse(nums, 1, 0)

        print("here...", dp_first, dp_second)

        return max(dp_first[-2], dp_second[-1])

