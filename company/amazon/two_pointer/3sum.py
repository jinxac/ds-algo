class Solution:
    def findNumber(self, nums, val, start, res):
        left = start
        right = len(nums) - 1
        
        while left < right:
            two_sum = nums[left] + nums[right]
            
            if two_sum == val:
                res.append([nums[left], -val, nums[right]])
                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left -1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                    
            elif two_sum < val:
                left += 1
            else:
                right -= 1
                
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            val = nums[i]
            self.findNumber(nums, -val, i+1, res)
        
        return res
            
        
