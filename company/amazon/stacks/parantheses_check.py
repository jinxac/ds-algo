class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        # () , {}, []
        
        temp = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for i in range(len(A)):
            if A[i] in ['(', '{' ,'[']:
                stack.append(A[i])
            elif len(stack) and temp[A[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(A[i])
        
        if len(stack) > 0:
            return 0
        
        return 1
                

