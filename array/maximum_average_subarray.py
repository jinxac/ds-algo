class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -100001
        start = 0
        end = 0
        temp = 0
        while end < len(nums):
            temp += nums[end]
            if end >= k - 1:
                res = max(temp / k, res)
                temp -= nums[start]
                start += 1

            end += 1

        return res