class Solution:
    def dfs(self, isConnected):
        visited = [0] * len(isConnected)
        res = 0
        
        def traverse(visited, i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    traverse(visited, j)
        
        for i in range(len(isConnected)):
            if visited[i] == 0:
                traverse(visited, i)
                res += 1
        
        return res
                
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        return self.dfs(isConnected)
