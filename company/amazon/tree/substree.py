# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if not root1 or not root2:
            return False
        
        return (
            self.isSameTree(root1.left, root2.left) and
            self.isSameTree(root1.right, root2.right) and
            root1.val == root2.val
        )
    
    
    def iterative(self, s, t):
        stack = []
        curr = s
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            
            if node.val == t.val and self.isSameTree(node, t):
                return True
            
            curr = node.right
        
        
        return False
    
    def recursive(self, s, t):
        def traverse(root):
            if root is None:
                return False
            
            l_same = traverse(root.left)
            r_same = traverse(root.right)
            
            is_same = False
            if root.val == t.val:
                is_same = self.isSameTree(root, t)
            
            return is_same or l_same or r_same
        
        return traverse(s)        
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.iterative(s, t)
        # return self.traverse(s, t)

