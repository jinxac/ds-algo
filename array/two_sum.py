"""
https://leetcode.com/problems/two-sum
"""

import collections

class Solution:

    def counter_approach(self, nums, target):
        counter = collections.Counter()
        res = []

        for i in range(len(nums)):
            if target - nums[i] in counter:
                # res += 1
                res.append(i)
                res.append(counter[target-nums[i]])
                counter[target-nums[i]] -= 1
                if counter[target-nums[i]] == 0:
                    del counter[target-nums[i]]
            else:
                counter[nums[i]] = i

        return res


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.counter_approach(nums, target)
        temp = {}
        # res = []
        count = 0

        for i in range(len(nums)):
            temp[nums[i]] = i


        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in temp and i != temp[diff]:
                # res.extend([i, temp[diff]])
                count += 1
                del temp[nums[i]]

        return count

