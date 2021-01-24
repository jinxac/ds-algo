'''
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        dq = deque()
        res = []

        if not root:
            return res

        dq.append(root)

        while dq:
            dq_size = len(dq)
            temp = []

            for i in range(dq_size):
                node = dq.pop()
                for i in range(len(node.children)):
                    dq.appendleft(node.children[i])

                temp.append(node.val)

            res.append(temp)

        return res

