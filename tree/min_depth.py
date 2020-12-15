"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""


class Solution:
  def dfs(self):
    if not root:
        return 0

    def traverse(root):
        if root is None:
            return 0

        if root.left is None or root.right is None:
            return  max(traverse(root.left), traverse(root.right)) + 1

        return min(traverse(root.left), traverse(root.right)) + 1

    return traverse(root)

    def minDepth(self, root: TreeNode) -> int:
      return self.dfs(root)

