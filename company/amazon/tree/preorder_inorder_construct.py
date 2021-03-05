# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
            1. first element in preorder is root
            2. search root in inorder
                a. left indices of root index will be left side of tree
                b. right indices of root index will be right side of tree
            3. recurse on left and right
            
            
              
        '''
        # self.curr_index = 0
        d = {}
        for i, e in enumerate(inorder):
            d[e] = i
        
        self.curr_index = 0
        def traverse(start, end):
            if start > end:
                return None
            
            node = TreeNode(preorder[self.curr_index])
            self.curr_index = self.curr_index + 1
            index = d[node.val]

            node.left = traverse(start, index - 1)

            node.right = traverse(index + 1, end)
            
            return node
            
        return traverse(0, len(preorder) - 1)
