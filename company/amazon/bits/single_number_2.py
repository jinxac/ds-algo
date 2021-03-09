class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1<<i) == (1<<i):
                    count +=1
            
            res = res | (count % 3) << i
        
        if res < (1 << 31):
            return res
        
        return res - (1 << 32)
