'''
https://leetcode.com/problems/binary-tree-right-side-view/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        dq = deque()
        res = []

        if not root:
            return []

        dq.append(root)

        while dq:
            dq_size = len(dq)
            temp = -1

            for i in range(dq_size):
                node = dq.pop()
                if node.left:
                    dq.appendleft(node.left)
                if node.right:
                    dq.appendleft(node.right)

                temp = node.val

            res.append(temp)

        return res

