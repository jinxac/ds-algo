# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import deque

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        dq = deque()
        dq.append(root)
        
        while dq:
            dq_size = len(dq)
            temp = []
            for i in range(dq_size):
                element = dq.pop()
                if element.left:
                    dq.appendleft(element.left)
                if element.right:
                    dq.appendleft(element.right)
                
                temp.append(element)
            
            for i in range(len(temp) -1):
                temp[i].next = temp[i+1]
            
            temp[len(temp) - 1].next = None
        
        
        return root        
        
        

