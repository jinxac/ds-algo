# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        dq = deque()
        if not A:
            return 1
        
        dq.appendleft(A)
        dq.appendleft(B)
        
        while dq:
            n1 = dq.pop()
            n2 = dq.pop()
            if n1.val != n2.val:
                return 0
            
            if n1.left and n2.left:
                dq.appendleft(n1.left)
                dq.appendleft(n2.left)
            elif n1.left or n2.left:
                return 0
            
            if n1.right and n2.right:
                dq.appendleft(n1.right)
                dq.appendleft(n2.right)
            elif n1.right or n2.right:
                return 0
        
        return 1
        

