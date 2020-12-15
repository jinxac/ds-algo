"""
https://leetcode.com/problems/find-the-duplicate-number/a
"""

class Solution:
    def hash_map_approach(self, nums):
        # temp_map = {x: nums.count(x) for x in nums}
        temp_map = {}
        for element in nums:
            if element in temp_map:
                return element
            else:
                temp_map[element] = 1

    def array_sort_approach(self, nums):
        # Time complexity: nlogn + n = O(nlogn), nums modified
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return nums[i]

    def cycle_approach(self, nums):
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break


        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


    def mutate_negative_approach(self, nums):

        for i in range(1,len(nums)):
            nums[abs(nums[i])] *= -1

        print(nums)


    def findDuplicate(self, nums: List[int]) -> int:
        # return self.hash_map_approach(nums)
        # return self.array_sort_approach(nums)
        # return self.hash_map_approach(nums)
        # return self.mutate_negative_approach(nums)
        return self.cycle_approach(nums)