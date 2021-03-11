class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, left, right):
            if len(curr) == 2 * n:
                res.append(''.join(curr[:]))
                return
            if left < n: 
                backtrack(curr + "(", left + 1, right)
            if right < left:
                backtrack(curr + ")", left, right + 1)
        
        backtrack( "", 0, 0)
        return res
