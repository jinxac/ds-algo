class Solution:
    def is_palindrome(self, s, start, end):
        return s[start:end+1] == s[start:end+1][::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        
        def helper(start, arr):
            if start >= len(s):
                self.res.append(arr[:])
                return
            
            for i in range(start, len(s)):
                if self.is_palindrome(s, start, i):
                    arr.append(s[start:i+1])
                    helper(i+1, arr)
                    arr.pop()
                    
        helper(0, [])
        return self.res
