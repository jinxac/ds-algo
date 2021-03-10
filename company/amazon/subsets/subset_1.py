class Solution:
    def recursive_solution(self, nums):
        def recurse(nums, start, res):
            if start == len(nums):
                return
            
            res_size = len(res)
            for r_index in range(res_size):
                temp = res[r_index] + [nums[start]]
                res.append(temp)
                
            recurse(nums, start + 1, res)
            
                
        
        res = [[]]
        recurse(nums, 0, res)
        return res
    
    def cascading(self, nums):
        result = [[]]
        
        for num in nums:
            result_size = len(result)
            for i in range(result_size):
                temp = result[i] + [num]
                result.append(temp)
        
        return result
    
    def backtracking(self, nums):
        result = []
        def backtrack(pos, start=0, curr=[]):
            if len(curr) == pos:
                print("pos", curr)
                result.append(curr[:])
                return
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(pos, i + 1, curr)
                curr.pop()
        
        for i in range(len(nums)+1):
            backtrack(i)
        
        return result
    
    def bitmask_approach(self, nums):
        res = []
        
        for i in range(2 ** len(nums), 2 ** (len(nums)+1)):
            bin_i = bin(i)[3:]
            temp = []
            for index, element in enumerate(bin_i):
                if element == '1':
                    temp.append(nums[index])
            res.append(temp)
        return res
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.bitmask_approach(nums)

            
