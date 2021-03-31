# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        def helper(root, arr, res):
            if root is None:
                return
            
            arr.append(root.val)
            if root.val == B:
                res.extend(arr[:])
                return
            
            helper(root.left, arr, res)
            helper(root.right, arr, res)
            arr.pop()
        
        
        arr = []
        res = []
        helper(A, arr, res)
        return res

