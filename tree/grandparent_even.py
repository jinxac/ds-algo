# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        def traverse(root):
            if root is None:
                return 0

            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        self.sum += root.left.left.val
                    if root.left.right:
                        self.sum += root.left.right.val

                if root.right:
                    if root.right.left:
                        self.sum += root.right.left.val
                    if root.right.right:
                        self.sum += root.right.right.val

            traverse(root.left)
            traverse(root.right)

            return root.val

        traverse(root)
        return self.sum