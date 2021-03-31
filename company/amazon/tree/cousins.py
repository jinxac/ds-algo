# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        dq = deque()
        res = []
        
        if A.val == B:
            return res
        
        if not A:
            return res
            
        '''
               1
             /   \
            2     3
           / \   / \
          4   5 6   7 
        '''
        dq.appendleft(A)
        
        while dq:
            dq_size = len(dq)
            temp = []
            is_match = False
            for _ in range(dq_size):
                node = dq.pop()
                if (node.left and node.left.val == B) or (node.right and node.right.val == B):
                    is_match = True
                    continue
                if node.left:
                    dq.appendleft(node.left)
                if node.right:
                    dq.appendleft(node.right)
                    
                
                temp.append(node.val)
            
            if is_match:
                return [x.val for x in dq]
