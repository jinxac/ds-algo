class Solution:
    def recursive(self, nums, total_sum, pos, dp):
        if total_sum == 0:
            return True

        if pos >= len(nums):
            return False
        
        if dp[pos][total_sum] != -1:
            return dp[pos][total_sum]
        
        if nums[pos] <= total_sum:
            if self.recursive(nums, total_sum - nums[pos], pos + 1, dp):
                dp[pos][total_sum] = True
                return dp[pos][total_sum]
            
            
        dp[pos][total_sum] = self.recursive(nums, total_sum, pos + 1, dp)
        return dp[pos][total_sum]
    
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        total_sum = total_sum // 2
        dp = [[]] * len(nums)
        
        for i in range(len(nums)):
            dp[i] = [-1] * (total_sum + 1)
        
        
        return self.recursive(nums, total_sum, 0, dp)
