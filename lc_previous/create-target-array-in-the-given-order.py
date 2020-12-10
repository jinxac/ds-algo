class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        len_nums = len(nums)
        res = []
        
        for i in range(len_nums):
            res.insert(index[i], nums[i])
        return res
        
        # for i in range(len(index)):
        #     res = res[:index[i]] + [nums[i]] + res[index[i]:]
        # return res
