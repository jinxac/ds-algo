"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.max = 0
    
    def maxDepthRecursive(self, root, d):
        if root is None:
            return 0

        for element in root.children:
            self.maxDepthRecursive(element, d + 1)
            self.max = max(self.max, d+1)
        
        
    def maxDepthIterative(self, root):
        stack = [root]
        d = 0
        while stack:
            node = stack.pop()
            if node:
                len_children = len(node.children) - 1
                if len_children >= 0:
                    print("here",node.val, d)
                    self.max = max(self.max, d)
                    d += 1
                    while len_children >= 0:
                        stack.append(node.children[len_children])
                        len_children -= 1
                else:
                    d = 0
                
    
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        self.maxDepthRecursive(root, 0)
        # self.maxDepthIterative(root)
        return self.max + 1

            
            
