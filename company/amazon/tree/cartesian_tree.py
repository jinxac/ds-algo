# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    
    '''
    {1, 5, 10, 40, 30, 15, 28, 20}
    
    helper(0, 7)
      -> max_value = 40
      -> max_index = 3
      -> node = 40
      -> node.left = helper(0, 3)
      -> node.right = helper(4, 7)
      -> return 40
     
     
    helper(0, 3)
      -> max_value = 10
      -> max_index = 2
      -> node = 10
      -> node.left = helper(0, 2)
      -> node.right = helper(3, 3)
      
    helper(0,2)
      -> max_value = 5
      -> max_index = 1
      -> node = 5
      -> node.left = helper(0, 1)
      -> node.right = helper(2, 2)
      -> return 5
     
     helper(0,1)
      -> max_value = 1
      -> max_index = 0
      -> node = 1
      -> node.left = helper(0, 0)
      -> node.right = helper(1, 1)
    
    '''
    def buildTree(self, A):
        def helper(start, end):
            if start >= end:
                return
            
            max_value = max(A[start:end])
            max_index = A.index(max_value)
            
            node = TreeNode(max_value)
            node.left = helper(start, max_index)
            node.right = helper(max_index +1, end)
        
            return node
        
        return helper(0, len(A))
