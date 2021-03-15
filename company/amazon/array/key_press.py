class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        '''
            1. Iterate over array and check for diff.
            2. If diff is larger assign to result
            3. If diff is equal check for key
            
            Will need 2 variables, res and key
            
            Time Complexity - O(n)
            Space - O(1)
        '''
        
        res = releaseTimes[0]
        key = keysPressed[0]
        
        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if diff > res:
                res = diff
                key = keysPressed[i]
            elif diff == res and keysPressed[i] > key:
                key = keysPressed[i]
        
        return key
        
