from heapq import *

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minHeap = []
        res = 0
        
        for i in range(len(sticks)):
            heappush(minHeap, sticks[i])
        
        while len(minHeap) > 1:
            e1 = heappop(minHeap)
            e2 = heappop(minHeap)
            
            curr_sum = e1 + e2
            res += curr_sum
            
            heappush(minHeap, curr_sum)
        
        return res
