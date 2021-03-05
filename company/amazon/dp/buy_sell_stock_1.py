class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        min_element = float('inf')
        res = float('-inf')
        
        for i in range(len(A)):
            if A[i] < min_element:
                min_element = A[i]
            else:
                res = max(res, A[i] - min_element)
        
        if res == float('-inf'):
            return 0
            
        return res

