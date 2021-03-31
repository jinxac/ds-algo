# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        dq = deque()
        res = []
        if not A:
            return res
        
        dq.appendleft(A)
        row = 1
        
        while dq:
            dq_size = len(dq)
            temp = []
            
            for _ in range(dq_size):
                node = dq.pop()
                if node.left:
                    dq.appendleft(node.left)
                if node.right:
                    dq.appendleft(node.right)
            
                if row % 2 == 0:
                    temp = [node.val] + temp
                else:
                    temp.append(node.val)
                
            row += 1
            res.append(temp)
        
        return res
                
        

