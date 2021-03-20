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
    def tree_to_dll(self, A):
        if A is None:
            return None, None
        
        self.first, self.last = None, None
        
        def helper(root):
            if root is None:
                return
            
            helper(root.left)
            
            if self.last:
                self.last.right = root
                root.left = self.last
            else:
                self.first = root
            
            self.last = root
            
            helper(root.right)
        
        helper(A)
        return self.first, self.last
    
    def dll_sum_search(self, first, last, B):
        while first != last:
            s = first.val + last.val
            
            if s == B:
                return 1
            
            if s > B:
                last = last.left
            else:
                first = first.right
            
        return 0
    
    def t2Sum(self, A, B):
        first, last = self.tree_to_dll(A)
        if not first and last:
            return 0
            
        return self.dll_sum_search(first, last, B)
