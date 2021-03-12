from collections import deque

class Solution:
    def build_array(self, s, arr):
        p1 = 0
        while p1 < len(s):
            temp = ""
            while p1 < len(s) and s[p1] != ' ':
                temp += s[p1]
                p1 += 1
            arr.appendleft(temp)
            while p1 < len(s) and s[p1] == ' ':
                p1 += 1        
                
            
    def solve(self, s: str) -> str:
        '''
            1. Remove leading spaces
            2. Remove trailing spaces
            3. Split the string based on a space
            4.
        '''
        
        # stripping left and right
        s = s.lstrip(' ')
        s = s.rstrip(' ')
        
        arr = deque()
        self.build_array(s, arr) 
        res = ""
        
        for i in range(len(arr)):
            res += arr[i]
            if i < len(arr) - 1:
                res += " "
        
        return res
                
                
            
