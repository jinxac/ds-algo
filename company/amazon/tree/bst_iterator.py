# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self._stack = []
        self.build_left(root)
    
    def build_left(self, root):
        while root:
            self._stack.append(root)
            root = root.left
        
        

    def next(self) -> int:
        node = self._stack.pop()
        if node.right:
            self.build_left(node.right)
        
        return node.val
        

    def hasNext(self) -> bool:
        return self._stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
