class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        if not A:
            return 0
        
        temp = {}
        start = 0
        end = 0
        res = 0
        
        while end < len(A):
            while A[end] in temp:
                res = max(res, end - start)
                temp[A[start]] -= 1
                if temp[A[start]] == 0:
                    del temp[A[start]]
                start += 1
            
            temp[A[end]] = 1
            end += 1
        
        res = max(res, end - start)
        return res
