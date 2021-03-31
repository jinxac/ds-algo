# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        
        '''
            4
           / \
          2    5
         / \  / \
        1   3 6  7
        
        [4,2,1,3,5,6,7]
        
        '''
        if root is None:
            return "X"
        
        '''
          // 4,2,1,3,5,6,7
        '''
        
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        dq = deque(data.split(','))
        
        def traverse():
            element = dq.popleft()
            if element == 'X':
                return None
            
            node = TreeNode(element)
            node.left = traverse()
            node.right = traverse()
            
            return node
        return traverse()
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    '''
       1
      / \
     2   3
        / \
       4   5
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        if not root:
            return res
        
        dq = deque()
        dq.append(root)
        
        while dq:
            node = dq.pop()
            if node:
                res += str(node.val) + ','
                dq.appendleft(node.left)
                dq.appendleft(node.right)
            else:
                res += 'X' + ','
        
        return res[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        s_data = data.split(',')
        dq = deque()
        
        n = TreeNode(s_data[0])
        dq.appendleft(n)
        start = 1
        
        while dq:
            node = dq.pop()
            if s_data[start] != 'X':
                l_node = TreeNode(s_data[start])
                node.left = l_node
                dq.appendleft(l_node)
            
            start += 1
            
            if s_data[start] != 'X':
                r_node = TreeNode(s_data[start])
                node.right = r_node
                dq.appendleft(r_node)
            start += 1
        
        return n
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
