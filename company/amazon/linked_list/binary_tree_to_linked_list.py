# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    
    def iterative(self, A):
        stck = [A]
        
        curr = None
        
        while stck:
            node = stck.pop()
            if not node:
                continue
            
            if node.right:
                stck.append(node.right)
            
            if node.left:
                stck.append(node.left)
            
            
            node.left = None
            if not curr:
                curr = node
            else:
                curr.right = node
                curr = curr.right
        
    def recursive(self, A):
        def helper(A):
            if not A.left:
                return
            
            temp = A.right
            A.right = A.left
            A.left = None
            
            while A.right:
                A = A.right
            
            A.right = temp
            
            
        def traverse(A):
            if A is None:
                return
            
            if A.right is None and A.left is None:
                return
            
            traverse(A.left)
            traverse(A.right)
            helper(A)
        
        traverse(A)
            
    def flatten(self, A):
        # self.iterative(A)
        self.recursive(A)
        return A
        # return self.recursive(A)
