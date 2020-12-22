"""
https://leetcode.com/problems/house-robber-iii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        self.map = {}

        def traverse(root):
            if root is None:
                return 0

            if root in self.map:
                return self.map[root]

            val = 0

            if root.left:
                val += traverse(root.left.left) + traverse(root.left.right)

            if root.right:
                val += traverse(root.right.left) + traverse(root.right.right)

            val = max(val + root.val, traverse(root.left) + traverse(root.right))
            self.map[root] = val
            return val

        return traverse(root)