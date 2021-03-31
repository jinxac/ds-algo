class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        res = []
        def helper(curr, left, right):
            if len(curr) == A * 2:
                res.append(curr)
            
            if left < A:
                helper(curr + '(', left + 1, right)
            
            if right < left:
                helper(curr + ')', left, right + 1)
        
        helper('', 0, 0)
        return res

