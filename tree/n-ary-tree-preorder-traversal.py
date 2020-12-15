"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.res = []
        
    def preordeIterative(self, root):
        if root is None:
            return
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            self.res.append(node.val)
            if node:
                len_children = len(node.children) - 1
                while len_children >= 0:
                    stack.append(node.children[len_children])
                    len_children -= 1
        
                    
        
    def preorderRecursive(self, root):
        if root is None:
            return

        self.res.append(root.val)

        for node in root.children:
            self.preorderRecursive(node)
        
   
    
    def preorder(self, root: 'Node') -> List[int]:
        # self.preorderRecursive(root)
        self.preordeIterative(root)
        return self.res
        
