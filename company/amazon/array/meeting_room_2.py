class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
         [[0,30], [5,15],[16,20]]
        
        # [15,30]
        
        '''
        
        intervals.sort(key=lambda x: x[0])
        
        res = 0
        temp = []
        
        for interval in intervals:
            end = interval[1]
            start = interval[0]
            pos = 0

            if not temp:
                temp.append(end)
                continue
            
            while pos < len(temp) and temp[pos] <= start:
                pos += 1
            
            if pos == 0:
                temp.append(end)
            else:
                temp[pos-1] = end
            
            temp.sort()
        
        return len(temp)
                
        
