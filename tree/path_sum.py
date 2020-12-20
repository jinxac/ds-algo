"""
https://leetcode.com/problems/path-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, root, sum):
        def traverse(root, s = 0):
            if root is None:
                return
            if root.left is None and root.right is None:
                if s + root.val == sum:
                    return True

                return False

            return traverse(root.left, s + root.val) or traverse(root.right, s + root.val)


        return traverse(root, 0)
        # return self.exists


    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.recur(root, sum)


