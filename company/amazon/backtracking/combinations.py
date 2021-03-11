class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, curr):
            if k == len(curr):
                res.append(curr[:])
                return
            
            for i in range(start, n+1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(1, [])
        return res
        
