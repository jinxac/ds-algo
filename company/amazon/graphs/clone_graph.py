"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs_recursion(self, node):
        def traverse(node, d):
            if not node:
                return None
            
            for nb in node.neighbors:
                if not nb in d:
                    d[nb] = Node(nb.val)
                    traverse(nb, d)
                
                d[nb].neighbors.append(d[node])
       
        if not node:
            return None
            
        d = {node: Node(node.val)}
        traverse(node, d)
        return d[node]
    
    def bfs(self, node):
        if not node:
            return None
        
        dq = deque()
        dc = {node: Node(node.val)}
        dq.append(node)
        
        while dq:
            curr_node = dq.popleft()
            for nb in curr_node.neighbors:
                if not nb in dc:
                    dc[nb] = Node(nb.val)
                    dq.append(nb)
                
                dc[nb].neighbors.append(dc[curr_node])
        
        return dc[node]
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.dfs_recursion(node)
