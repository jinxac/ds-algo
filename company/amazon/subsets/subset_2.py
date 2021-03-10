class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = [[]]
        prev = []
        start_index, end_index = 0, 0 
        
        for nums_index in range(len(nums)):
            start_index = 0
            if nums_index > 0 and nums[nums_index] == nums[nums_index-1]:
                start_index = end_index
            
            end_index = len(result)
            for res_index in range(start_index, end_index):
                temp = result[res_index] + [nums[nums_index]]
                result.append(temp)
        return result
