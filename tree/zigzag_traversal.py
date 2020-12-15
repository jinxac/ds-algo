"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result

        dq = deque()
        dq.append(root)
        level = False


        while dq:
            dq_size = len(dq)
            temp = deque()

            for _ in range(dq_size):
                element = dq.pop()
                if level:
                    temp.appendleft(element.val)
                else:
                    temp.append(element.val)

                if element.left:
                    dq.appendleft(element.left)
                if element.right:
                    dq.appendleft(element.right)

            level = not level
            result.append(list(temp))


        return result