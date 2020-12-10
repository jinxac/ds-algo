# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # Top down approach     
#     def maxDepth(self, root):
#         self.maximum = 0
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         def f(root, depth):
#             if root == None:
#                 return None
#             if not root.left and not root.right:
#                 self.maximum = max(self.maximum, depth)
            
#             f(root.left, depth+1)
#             f(root.right, depth+1)
        
#         if not root:
#             return 0
        
#         f(root, 1)
#         return self.maximum
    
    # Bottom up approach
    def maxDepth(self, root):
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right) + 1
                
            

        
