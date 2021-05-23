class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(pos,arr, result):
            if pos == len(graph) - 1:
                result.append(arr[:])
                return
            
            for j in graph[pos]:
                arr.append(j)
                helper(j, arr, result)
                arr.pop()
        
        result = []
        helper(0,[0], result)
        
        return result
