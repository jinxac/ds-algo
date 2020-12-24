"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.result = 0
        def traverse(root, curr_sum):
            if root is None:
                return

            curr_sum += root.val

            if root.left is None and root.right is None:
                self.result += curr_sum

            traverse(root.left, curr_sum * 10)
            traverse(root.right, curr_sum * 10)

        traverse(root, 0)
        return self.result