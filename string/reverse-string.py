class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        i = 0
        j = len(s) - 1
        
        
        while i < j:
            s[i],s[j] = s[j], s[i]
            i += 1
            j -= 1

        def reverse_str(s, start, end):
            if start > end:
                return
            
            s[start], s[end] = s[end], s[start]
            reverse_str(s, start + 1, end - 1)
        
        reverse_str(s, 0, len(s) - 1)
        
                    
