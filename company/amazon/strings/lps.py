class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        dp = []
        res = ""
        
        for i in range(len(A)):
            dp.append([0] * len(A))
        
        
        for col in range(len(A)):
            i = 0
            j = col
            
            while j < len(A):
                if col == 0:
                    dp[i][j] = 1
                
                elif col == 1:
                    if A[i] == A[j]:
                        dp[i][j] = 1
                
                elif A[i] == A[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                
                if dp[i][j] == 1:
                    temp = A[i:j+1]
                    if len(temp) > len(res):
                        res = temp
                
                i += 1
                j += 1
        
        return res
