'''
https://leetcode.com/problems/find-bottom-left-tree-value/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        dq = deque()
        res = 0

        if not root:
            return 0

        dq.append(root)

        while dq:
            dq_size = len(dq)
            temp = 0

            for i in range(dq_size):
                node = dq.pop()

                if node.right:
                    dq.appendleft(node.right)

                if node.left:
                    dq.appendleft(node.left)




                temp = node.val

            res = temp

        return res


