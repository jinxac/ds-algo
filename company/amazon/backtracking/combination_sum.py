class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, curr):
            sum_curr = sum(curr)
            if sum_curr >= target:
                if sum_curr== target:
                    res.append(curr[:])
                return
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr)
                curr.pop()
                    
        
        backtrack(0, [])
        
        return res
            
                
