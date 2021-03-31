class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        '''
            [1,2,3]
            
            -> helper(0)
                -> for i in range(0, 3)
                    A[0], A[0] = A[0], A[0]
                    helper(1)
                    A[0], A[0] = A[0], A[0]
                    
                    A[1], A[0] = A[ 
            
            -> helper(1)
                -> for i in range(1, 3)
                    A[1], A[1] = A[1], A[1]
                    helper(2)
                    A[1], A[1] = A[1], A[1]
                    
                    A[2], A[1] = A[1], A[2]
                    helper(3)
                    A[2], A[1] = A[1], A[2]
                
            
            -> helper(2)
                -> for i in range(2,3)
                    A[2], A[2] = A[2], A[2]
                    helper(3)
                    A[2], A[2] = A[2], A[2]
            
            -> helper(3)
                -> res = [1,2,3], [1,3,2]
                return
                
            
        '''
        
        res = []
        def helper(pos):
            if pos == len(A):
                res.append(A[:])
                return
                
            for i in range(pos, len(A)):
                A[pos], A[i] = A[i], A[pos]
                helper(pos + 1)
                A[i], A[pos] = A[pos], A[i]
        
        helper(0)
        return res
        
