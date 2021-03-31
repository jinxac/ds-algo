class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        '''
            disjoint
            sorted
            
            [[0,2],[5,10],[13,23],[24,25]]
            
            [[1,5],[8,12],[15,24],[25,26]]
            
            
            [[1,2], [5,5], [8,10],[15,23], [24,24],[25,25]]
            
            Logic:
             1. max(A[0], B[0]) to get the start, min(A[1], B[1]) to get the end
             2. if max(A[0], B[0]) < min(A[1], B[1]) increment the list with minimum B[1] else add to result
            
            
        '''
        
        p1 = 0
        p2 = 0
        res = []
        
        while p1 < len(A) and p2 < len(B):
            start = max(A[p1][0], B[p2][0])
            end = min(A[p1][1], B[p2][1])
            
                
            if end >= start:
                res.append([start, end])
            
            if B[p2][1] < A[p1][1]:
                p2 += 1
            else:
                p1 += 1
        
        return res
                
