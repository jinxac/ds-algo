class Solution:
    def dp_pattern(self, num):
        if num == 0:
            return [0]
        dp = [0] * (num+1)
        dp[1] = 1
        offset = 2
        
        for i in range(2, num + 1):
            div, mod = divmod(i, offset)
            if div > 1 and mod == 0:
                offset = offset * 2
            dp[i] = dp[i - offset] + 1
        
        return dp
    
    def dp_bitwise(self, num):
        if num == 0:
            return [0]
        
        dp = [0] * (num + 1)
        for i in range(1, len(dp)):
            # Getting the count of 1 bits in 0 to n-1 bits
            dp[i] = dp[i>>1]
            
            # Checking if last bit is 1 then adding that
            if (i&1) == 1:
                dp[i] += 1
        return dp
        
    
    def countBits(self, num: int) -> List[int]:
        return self.dp_bitwise(num)
