# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root, k):
        res = []
        def traverse(root):
            if root is None:
                return
            
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        
        traverse(root)
        
        return res[k - 1]
    
    def iterative(self, root, k):
        stack = []
        res = []
        
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            res.append(node.val)
            k -= 1
            
            if k == 0:
                break
            
            curr = node.right
        
        return res[-1]
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.iterative(root, k)
