class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        if not A:
            return 0
            
        if len(A) == 1:
            return A[0]
    
        max_val = A[0]
        min_val = A[0]
        res = float('-inf')
        
        for i in range(1, len(A)):
            curr_min = A[i] * min_val
            curr_max = A[i] * max_val
            max_val = max(A[i], curr_min, curr_max)
            min_val = min(A[i], curr_min, curr_max)
            res = max(max_val, min_val, res)
        
        return res

