# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def traverse(start, end):
            if end < start:
                return None
            
            
            mid = ((start + end) // 2)            
            node = TreeNode(nums[mid])
            node.left = traverse(start, mid - 1)
            node.right = traverse(mid + 1, end)
            
            return node
        
        return traverse(0, len(nums) - 1)
