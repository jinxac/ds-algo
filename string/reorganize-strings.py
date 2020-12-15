from collections import OrderedDict

class Solution:
    def reorganizeString(self, S: str) -> str:
        '''
            My Algorithm
            
            1. Iterate over string and store individual count in dict
            2. Sort dictionary by value
            3. Check first count, if > ceil(len(s) / 2) return ""
            4. Create an empty array of string length
            5. Iterate over map -> get key -> find empty space -> insert at alternate positions
            6. Check map, if empty return array as string else return ""
        '''
        
        
        '''
            Ideal algorithm Greedy + Heap Queue(Priority queue)
            Greedy because the next element chosen should not be equal to previous one
        '''
#         if not S or len(S):
#             return ""
        
        pq = [(-S.count(x), x) for x in set(S)]
        answer = ""
        heapq.heapify(pq)
 
        for nc, element in pq:
            if -nc > (len(S) + 1) / 2:
                return ""
        
        
        while len(pq) >= 2:
            c1, e1 = heapq.heappop(pq);
            c2, e2 = heapq.heappop(pq);
            
            answer += e1 + e2
            
            if c1 +1:
                heapq.heappush(pq, (c1+1, e1))
            
            if c2 + 1:
                heapq.heappush(pq, (c2+1, e2))
        
        return answer + (pq[0][1] if pq else '')
            
