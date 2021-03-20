from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._maxHeap = []
        self._minHeap = []
        

    def addNum(self, num: int) -> None:
        if not self._maxHeap or -self._maxHeap[0] > num:
            heappush(self._maxHeap, -num)
        else:
            heappush(self._minHeap, num)
        
        if len(self._maxHeap) - len(self._minHeap) > 1:
            heappush(self._minHeap, -heappop(self._maxHeap))
        elif len(self._maxHeap) < len(self._minHeap):
            heappush(self._maxHeap, -heappop(self._minHeap))
        

    def findMedian(self) -> float:
        if len(self._maxHeap) == len(self._minHeap):
            return (-self._maxHeap[0] + self._minHeap[0]) / 2
        
        return -self._maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
