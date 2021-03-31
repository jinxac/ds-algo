class Solution:
    def optimised(self, nums):
        nums = set(nums)
        res = 0
        
        for element in nums:
            if (element -1) in nums:
                continue
            start = element
            temp = 0
            while start in nums:
                temp += 1
                start += 1
            
            res = max(res, temp)
        
        return res
                
    def sorting(self, nums):
        nums = list(set(nums))
        nums.sort()
        start, end = 0, 0
        res = 0
        
        # [1,2,3,4,100,200]
        
        if len(nums) == 1:
            return 1
        
        while end < len(nums):
            while end > 0 and end < len(nums) and nums[end] == 1 + nums[end-1]:
                end += 1
            res = max(res, end - start)
            start = end
            end += 1
        
        return res
    
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.optimised(nums)
                
