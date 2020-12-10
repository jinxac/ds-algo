class Solution:
    
    def maxn3(self, nums):
        res = -1000000001
        n = len(nums)
        
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    temp = nums[i] * nums[j] * nums[k]
                    res = max(res, temp)
        
        return res
    
    def maxSort(self, nums):
        res = -1000000001
        n = len(nums)
        
        nums.sort()
        positive_max = nums[n-1] * nums[n-2] * nums[n-3]
        negative_max = nums[0] * nums[1] * nums[n-1]
        return max(positive_max, negative_max)
    
    
    def maximumProduct(self, nums: List[int]) -> int:
        '''
            Observations:
            1. Product will be max for max 3 numbers. First intuition says sort the array(reverse) and multiple top 3 numbers
            2. The above algo works fine in case numbers are positive, but in case of negative numbers this will fail, hence sorting will not work for these scenarios
            
            Approach:
            
            1. First approach is keep 3 variables i,j and k and check the products of all 3 pairs in the array. The efficiency of this is n^3 and hence got TLE on 63rd case
            2. Next approach can be to sort the array and find the product of last 3 numbers. This would work fine in case of positive numbers, but also 3 negative numbers can
               make a positive. Hence the result will be max of right most number * 2-left most numbers and 3 right most numbers
               
            Stuck:-
            
            1. Negative number scenario. Could not come up solution to handle 2 negative make positive number. Had to see solution for this
        '''
        return self.maxSort(nums)
        

                    
                    
