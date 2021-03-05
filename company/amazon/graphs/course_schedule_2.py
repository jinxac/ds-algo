from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        
        if numCourses <= 0:
            return result
        
        in_degree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}
        
        for p in prerequisites:
            parent, child = p[0], p[1]
            in_degree[child] += 1
            graph[parent].append(child)
        
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)
        
        while sources:
            vertex = sources.popleft()
            result.append(vertex)
            
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)
        
        if len(result) != numCourses:
            return []
        
        result.reverse()
        return result
        
