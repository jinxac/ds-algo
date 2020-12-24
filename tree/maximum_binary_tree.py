"""
https://leetcode.com/problems/maximum-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def get_max_element(self, nums, start, end):
        pos = -1
        max_element = -1
        for i in range(start, end + 1):
            if nums[i] > max_element:
                max_element = nums[i]
                pos = i

        return pos


    def build(self, root, nums, start, end):
        if root is None:
            return

        max_pos = self.get_max_element(nums, start, end)


        if max_pos == -1:
            return

        new_node = TreeNode(nums[max_pos])
        new_node.left = self.build(new_node, nums, start, max_pos - 1)
        new_node.right = self.build(new_node, nums, max_pos + 1, end)

        return new_node






    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        max_pos = self.get_max_element(nums, 0, len(nums) - 1)
        root = TreeNode(nums[max_pos])

        root.left = self.build(root, nums, 0, max_pos - 1)
        root.right = self.build(root, nums, max_pos + 1, len(nums) - 1)

        return root