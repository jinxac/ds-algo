# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        stack = []
        curr = A
        node = None
        res = []
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            if stack[-1].right and stack[-1].right != node:
                curr = stack[-1].right
            else:
                node = stack.pop()
                res.append(node.val)
        
        return res

