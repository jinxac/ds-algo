class Solution:
    def myApproach(self, num):
        res = ""
        while num > 0:
            res = str((num & 1) ^ 1) + res
            num = num >> 1

        return int(res, 2)    
    
    def myApproachSpaceEfficient(self, num):
        temp = num
        bit = 1
        
        while temp > 0:
            num = num ^ bit
            bit = bit << 1
            temp = temp >> 1
        
        return num
    
    
    def bitmask(self, num):
        len_num = math.floor(math.log(num, 2)) + 1
        mask_length = (1 << len_num) - 1
        
        return num ^ mask_length
            
    
    def inbuilt_bitmask(self, num):
        mask_length = (1 << num.bit_length()) - 1
        return num ^ mask_length
    
    
    # best way to generate bitmask
    def open_jdk_hacker_delight(self, num):
        bitmask = num
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        
        return bitmask ^ num
    
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        # return self.myApproach(num)
        # return self.myApproachSpaceEfficient(num)
        # return self.bitmask(num)
        # return self.inbuilt_bitmask(num)
        return self.open_jdk_hacker_delight(N)
