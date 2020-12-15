# Definition for a binary tree node.
# class TreeNode:
    # def __init__(self, x):
    #     self.val = x
    #     self.left = None
    #     self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if(t1 == None):
            return t2

        if(t2 == None):
            return t1

        t1.val = t1.val + t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1
#         if t1 == None and t2 == None:
#             return None;

#         val = 0
#         if t1 == None:
#             val = t2.val
#             t1_left = None
#             t1_right = None
#             t2_left = t2.left
#             t2_right = t2.right
#         elif t2 == None:
#             val = t1.val
#             t2_left = None
#             t2_right = None
#             t1_left = t1.left
#             t1_right = t1.right
#         else:
#             val = t1.val + t2.val
#             t2_left = t2.left
#             t2_right = t2.right
#             t1_left = t1.left
#             t1_right = t1.right
        
#         t = TreeNode(val)
#         t.left = self.mergeTrees(t1_left, t2_left)
#         t.right = self.mergeTrees(t1_right, t2_right)
#         return t
