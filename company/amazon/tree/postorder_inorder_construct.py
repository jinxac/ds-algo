# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        d = {}
        for i, e in enumerate(inorder):
            d[e] = i
            
        self.post_index = len(postorder) - 1    
        
        def traverse(start, end):
            if start > end:
                return None
            
            node = TreeNode(postorder[self.post_index])
            self.post_index -= 1
            
            mid = d[node.val]
            
            node.right = traverse(mid+1, end)
            node.left = traverse(start, mid - 1) 
            
            return node
        
        return traverse(0, len(postorder) - 1)
