class Solution:
    
    def canPlace(self, arr, row, col):
        # Checking col
        for j in range(len(arr)):
            if arr[row][j] == 'Q':
                return False
        
        # Checking row
        for i in range(len(arr)):
            if arr[i][col] == 'Q':
                return False
        
        # Checking digonal
        i = row
        j = col
        
        while i >= 0 and j >= 0:
            if arr[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        i = row
        j = col
        
        while i < len(arr) and j < len(arr):
            if arr[i][j] == 'Q':
                return False
            
            i += 1
            j += 1
        
        
        
        # Checking anti diagonal
        i = row
        j = col
        
        while i >= 0 and j < len(arr):
            if arr[i][j] == 'Q':
                return False
            
            i -= 1
            j += 1
        
        i = row
        j = col
        
        while i < len(arr) and j >= 0:
            if arr[i][j] == 'Q':
                return False
            
            i += 1
            j -= 1
            
            
        return True
    
    def solve(self, row, arr, size, res):
        if size == row:
            res.append([''.join(datum) for datum in arr])
            return
        
        for j in range(len(arr)):
            if arr[row][j] == '.':
                if self.canPlace(arr, row, j):
                    arr[row][j] = 'Q'
                    self.solve(row+1, arr, size, res)
                    arr[row][j] = '.'   
        
                 
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = []
        res = []
        for i in range(n):
            arr.append(['.'] * n)
            
        self.solve(0, arr, n, res)
        return res
