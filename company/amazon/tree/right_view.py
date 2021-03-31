# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
from collections import deque
 
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        dq = deque()
        res = []
        if not A:
            return res
        
        dq.appendleft(A)
        
        while dq:
            dq_size = len(dq)
            temp = -1
            
            for _ in range(dq_size):
                node = dq.pop()
                if node.left:
                    dq.appendleft(node.left)
                if node.right:
                    dq.appendleft(node.right)
                
                temp = node.val
            
            res.append(temp)
        
        return res
