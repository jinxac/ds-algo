class Solution:
    def generateSolutionN2(self,nums):
        len_nums = len(nums)
        res = [0] * (len(nums))
        
        for i in range(len_nums):
            for j in range(len_nums):
                if i == j:
                    continue
                if nums[i] > nums[j]:
                    res[i] += 1
        
        return res

    
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return self.generateSolutionN2(nums)
    
        
