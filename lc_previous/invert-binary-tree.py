# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root is None:
                return None
            
            if root.left is None and root.right is None:
                return root
            
            
            invert(root.left)
            invert(root.right)

            temp = root.left
            root.left = root.right
            root.right = temp
            
            return root
        
        return invert(root)
