# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recursive(self, root):
        def traverse(root):
            if root is None:
                return 0, True
            
            l_h, is_l_valid = traverse(root.left)
            r_h, is_r_valid = traverse(root.right)
            
            is_valid = is_l_valid and is_r_valid and abs(l_h - r_h) <= 1
            
            return max(l_h, r_h) + 1, is_valid
    
        res = traverse(root)[1]
        
        if res:
            return 1
        
        return 0
        
        
        
    def isBalanced(self, root):
        return self.recursive(root)

