"""
https://leetcode.com/problems/binary-tree-paths/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, arr, result):
        if root is None:
            return

        arr.append(root.val)

        if root.left is None and root.right is None:
            temp = [str(x) for x in arr[:]]

            temp_str = '->'.join(temp)

            result.append(temp_str)

        self.traverse(root.left, arr, result)
        self.traverse(root.right, arr, result)

        arr.pop()

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        self.traverse(root, [], result)
        return result