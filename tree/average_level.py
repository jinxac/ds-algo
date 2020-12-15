"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""

import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        if not root:
            return res
        dq = deque()
        dq.append(root)

        while dq:
            dq_size = len(dq)
            temp = 0

            for _ in range(dq_size):
                element = dq.pop()
                temp += element.val
                if element.left:
                    dq.appendleft(element.left)

                if element.right:
                    dq.appendleft(element.right)

            res.append(temp / dq_size)

        return res
