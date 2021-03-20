# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def build_parent_obj(self, root):
        parent_node = {}
        def traverse(root, obj):
            if root is None:
                return None
            
            
            l = traverse(root.left, obj)
            r = traverse(root.right, obj)
            
            if l:
                parent_node[l] = root
            if r:
                parent_node[r] = root            
            return root
        
        traverse(root, parent_node)
        parent_node[root] = None
        return parent_node
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parent_map = self.build_parent_obj(root)
        
        seen = {}
        
        dq = deque()
        dq.appendleft(target)
        seen[target] = None

        
        while dq:
            dq_size = len(dq)
            temp = []
            
            for _ in range(dq_size):
                node = dq.pop()
                if node.left and not node.left in seen:
                    dq.appendleft(node.left)
                    seen[node.left] = None
                if node.right and not node.right in seen:
                    dq.appendleft(node.right)
                    seen[node.right] = None
                
                if parent_map[node] and not parent_map[node] in seen:
                    dq.appendleft(parent_map[node])
                    seen[parent_map[node]] = None
                temp.append(node.val)
            
            K -= 1
            
            if K < 0:
                return temp
        
        return []
