from heapq import *
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for point in points:
            diff = math.sqrt(point[0] * point[0] + point[1] * point[1])
            heappush(minHeap, (-diff, point))
            
            if len(minHeap) > k:
                heappop(minHeap)
        
        res =[datum[1] for datum in minHeap]
        
        return res
