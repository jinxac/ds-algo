class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        def search(root): 
            if root is None:
                return None
            
            
            if root.val == val:
                return root

            elif root.val > val:
                return search(root.left)
            else:
                return search(root.right)
        
        return search(root)     
