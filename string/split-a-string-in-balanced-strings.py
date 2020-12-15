class Solution:
    def balancedStringSplit(self, s: str) -> int:
        '''
            Intuition
            
            Increment count for R and decrement for L, when 0 increment result
        '''
        
        cnt = 0
        res = 0
        for element in s:
            if element == 'R':
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                res += 1
        
        return res
        
