class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        if len(arr) == 1:
            if len(arr[0]) == len(set(arr[0])):
                return len(arr[0])
            
            return 0
        
        self.max = 0
        
        def helper(size, pos, curr):
            if len(curr) == size:
                temp = ''.join(curr)
                if len(temp) == len(set(temp)):
                    self.max = max(self.max, len(temp))
                return
            
            for i in range(pos, len(arr)):
                curr.append(arr[i])
                helper(size, i + 1, curr)
                curr.pop()
                
                
        for i in range(1, len(arr) + 1):
            helper(i, 0, [])
        
        
        return self.max
