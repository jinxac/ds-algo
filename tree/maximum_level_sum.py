'''
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        dq = deque()
        res = []
        level = 1
        max_res = -float('inf')
        result = 0

        if not root:
            return 0

        dq.append(root)

        while dq:
            dq_size = len(dq)
            temp = 0

            for _ in range(dq_size):
                node = dq.pop()
                if node.left:
                    dq.appendleft(node.left)

                if node.right:
                    dq.appendleft(node.right)

                temp += node.val

            if temp > max_res:
                max_res = temp
                result = level
            level += 1

        return result

