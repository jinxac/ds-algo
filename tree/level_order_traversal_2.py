from collections import deque

"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

#
#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = deque()
        dq = deque()
        dq.append(root)

        while dq:
            size = len(dq)
            temp = []
            for _ in range(size):
                element = dq.pop()
                temp.append(element.val)

                if element.left:
                    dq.appendleft(element.left)

                if element.right:
                    dq.appendleft(element.right)

            res.appendleft(temp)

        return res
