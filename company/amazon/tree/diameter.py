# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        self.diameter = float('-inf')
        def helper(root):
            if root is None:
                return 0
            
            l_height = helper(root.left)
            r_height = helper(root.right)
            
            self.diameter = max(self.diameter, l_height + r_height)
            
            return max(l_height, r_height) + 1
        
        helper(root)
        
        
        return self.diameter
