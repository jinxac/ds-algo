# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.reference = None
        
        def getRef(original, cloned):
            if not original and not cloned:
                return
            
            if original == target:
                self.reference = cloned
            
            getRef(original.left, cloned.left)
            getRef(original.right,cloned.right)
            
        getRef(original, cloned)
        
        return self.reference
