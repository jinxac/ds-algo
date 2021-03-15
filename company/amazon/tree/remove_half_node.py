# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        def traverse(root):
            if root is None:
                return
            
            
            if root.left is None and root.right is None:
                return
            
            traverse(root.left)
            traverse(root.right)
            
            if root.left and root.left.left and not root.left.right:
                root.left = root.left.left
            
            if root.left and root.left.right and not root.left.left:
                root.left = root.left.right
            
            if root.right and root.right.left and not root.right.right:
                root.right = root.right.left
            
            if root.right and root.right.right and not root.right.left:
                root.right = root.right.right
                
        traverse(A)
        return A


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, n):
        def traverse(root):
            if root is None:
                return None
            
            root.left = traverse(root.left)
            root.right = traverse(root.right)
            
            if bool(root.left) == bool(root.right):
                return root
            
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left
            
                
        traverse(n)
        return n

