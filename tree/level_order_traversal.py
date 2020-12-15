"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dq = deque()
        dq.append(root)
        res = []


        while dq:
            dq_size = len(dq)
            temp = []
            for _ in range(dq_size):
                element = dq.pop()
                temp.append(element.val)
                if element.left:
                    dq.appendleft(element.left)
                if element.right:
                    dq.appendleft(element.right)

            res.append(temp)

        return res
