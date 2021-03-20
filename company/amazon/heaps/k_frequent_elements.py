from heapq import *

class Custom:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        
        return self.count < other.count


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        minHeap = []
        res = []
        
        for key, value in c.items():
            heappush(minHeap, Custom(key, value))
            
            if len(minHeap) > k:
                heappop(minHeap)
                    
        while minHeap:
            res = [heappop(minHeap).word] + res
        
        return res
