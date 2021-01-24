'''
https://leetcode.com/problems/binary-tree-preorder-traversal/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        stack.append(root)
        res = []

        while stack:
            element = stack.pop()
            if element:
                res.append(element.val)

            if element.right:
                stack.append(element.right)

            if element.left:
                stack.append(element.left)

        return res

