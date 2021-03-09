# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "X"
        
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        datum = data.split(",")
        dq = deque(datum)
        
        node = TreeNode(0)
    

        def traverse():
            element = dq.popleft()
            
            if element == 'X':
                return None
            
            node = TreeNode(int(element))
            
            node.left  = traverse() 
            node.right = traverse()
            
            return node
        
        return traverse()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
