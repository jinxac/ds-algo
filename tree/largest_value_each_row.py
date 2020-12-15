# Definition for a binary tree node.
"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""

from collections import deque
import math




# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        dq = deque()
        dq.append(root)

        while dq:
            dq_size = len(dq)
            max_value = -math.inf

            for _ in range(dq_size):
                element = dq.pop()
                max_value = max(element.val, max_value)
                if element.left:
                    dq.appendleft(element.left)

                if element.right:
                    dq.appendleft(element.right)

            result.append(max_value)

        return result


