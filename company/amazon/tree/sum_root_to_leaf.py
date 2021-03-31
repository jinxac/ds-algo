# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        self.totalSum = 0
        def helper(root, curr):
            if root is None:
                return 0
            
            if root.left is None and root.right is None:
                # print("here", arr)                curr += str(root.val)
                self.totalSum += int(curr)
                return
            
            helper(root.left, curr + str(root.val))
            helper(root.right, curr + str(root.val))
        
        helper(A, "")
        return self.totalSum % 1003

