# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
        Algorithms
            1. Recursive
            2. Iterative
            
        Logic is same for both recursive and iterative. Following is the logic:-
        
        1. Check if root lies in the range of [L, R], if it does add to res
        2. Check if L is less than root, if yes check root.left
        3. Check if R is greater than root, if yes check root.right
        
        Complexity: 
        
            Time O(n)
            Space O(n)
    '''
    def __init__(self):
        self.res = 0
        
    def getRecursive(self, root, L, R):
        if root is None:
            return 
        
        if L <= root.val <= R:
            self.res += root.val
        
        if L < root.val:
            self.getRecursive(root.left, L, R)
        if R > root.val:
            self.getRecursive(root.right, L, R)
            
    def getIterative(self, root, L, R):
        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    res += node.val

                if L < node.val:
                    stack.append(node.left)

                if R > node.val:
                    stack.append(node.right)
        
        return res
            
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # self.getRecursive(root, L, R)
        # return self.res
        return self.getIterative(root, L, R)
