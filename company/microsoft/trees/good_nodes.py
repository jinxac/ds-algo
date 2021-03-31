# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = []
        max_stack = []
        curr = root 
        res = 0
        node = None
        
        while stack or curr:
            while curr:
                stack.append(curr)
                if not max_stack:
                    max_stack.append(curr.val)
                    res += 1
                elif curr.val >= max_stack[-1]:
                    res += 1
                    max_stack.append(curr.val)
                else:
                    max_stack.append(max_stack[-1])
                
                curr = curr.left
            
            if stack[-1].right and node != stack[-1].right:
                curr = stack[-1].right
            else:
                node = stack.pop()
                max_stack.pop()
                
        
        return res
                
