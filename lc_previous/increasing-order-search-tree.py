# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        '''
            Testcases checked:
            
            1. Empty left
            2. Empty Right
            3. Single node
        '''
        temp = []
        
        def in_order(root):
            if root is None:
                return None
            
            in_order(root.left)
            temp.append(root.val)
            in_order(root.right)

        in_order(root)
        
        g = TreeNode(temp[0])
        
        def generate_tree(root, index):
            if index >= len(temp):
                return
            
            root.right = TreeNode(temp[index])
            return generate_tree(root.right, index + 1)
        
        generate_tree(g, 1)
        
        return g
            
