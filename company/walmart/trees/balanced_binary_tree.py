"""
https://leetcode.com/problems/balanced-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.is_balanced = True

        def traverse(root):
            if root is None:
                return 0

            l_height = traverse(root.left)
            r_height = traverse(root.right)

            if abs(r_height - l_height) > 1:
                self.is_balanced = False

            return max(l_height, r_height) + 1

        traverse(root)
        return self.is_balanced
