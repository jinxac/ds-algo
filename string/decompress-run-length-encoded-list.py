class Solution:
    def whileSolution(self, nums):
        i = 0
        res = []
        while i < len(nums) - 1:
            freq, val = nums[i], nums[i+1]

            temp = [val] * freq
            res.extend(temp)

            i += 2
        return res
    
    def rangeFor(self, nums):
        res = []
        for i in range(0, len(nums) -1, 2):
            res += [nums[i+1]] * nums[i]
        
        return res
    
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # return self.whileSolution(nums)
        return self.rangeFor(nums)
