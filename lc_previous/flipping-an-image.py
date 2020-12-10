class Solution:
    '''
        Check for optimisation
    '''
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def flip(row):
            i = 0
            j = len(row) - 1
            
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
        
        
        def invert():
            for i in range(len(A)):
                for j in range(len(A)):
                    if A[i][j] == 1:
                        A[i][j] = 0
                    elif A[i][j] == 0:
                        A[i][j] = 1
        
        for row in A:
            flip(row)
            
        invert()
        
        return A
    
