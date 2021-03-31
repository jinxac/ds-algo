# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        '''
                      5
                     / \
                    4   8
                   /   / \
                  11  13  4
                 /  \      \
                7    2      1
        '''
        def helper(root, curr):
            if root is None:
                return 0
            
            if root.left is None and root.right is None:
                if curr == root.val:
                    return 1
                
                return 0
            
            return helper(root.left, curr - root.val) or helper(root.right, curr - root.val)
        
        return helper(A, B)

