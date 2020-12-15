# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.sum = 0        
        
        def getHeight(root):
            if root is None:
                return 0
            
            return 1 + max(getHeight(root.left), getHeight(root.right))
        
        
        self.height = getHeight(root)   
            
        
        def getSum(root, count):
            if root is None:
                return None
            if root.right is None and root.left is None:
                if count == self.height - 1:
                    self.sum += root.val
                return None
            
            getSum(root.left, count + 1)
            getSum(root.right, count + 1)
        
        
        getSum(root, 0)
        
        return self.sum
        
