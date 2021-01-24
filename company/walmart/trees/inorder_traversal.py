'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root):
        res = []
        def traverse(root):
            if root is None:
                return

            traverse(root.left)
            res.append(root.val)
            traverse(root.right)

        traverse(root)
        return res


    def iterative(self, root):
        stack = []
        res = []
        curr = root

        while stack or curr:
            while curr != None:
                stack.append(curr)
                curr = curr.left

            element = stack.pop()
            res.append(element.val)
            curr = element.right
        return res





    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.iterative(root)
