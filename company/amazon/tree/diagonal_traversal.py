# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if A is None:
            return []
        
        self.temp = {}
        res = []
        
        def helper(root, x):
            if root is None:
                return

            if not x in self.temp:
                self.temp[x] = []
            self.temp[x].append(root.val)
        
            helper(root.left, x+1)
            helper(root.right, x)
            
        helper(A, 0)
        
        for value in self.temp.values():
            res.extend(value)
            
        return res

