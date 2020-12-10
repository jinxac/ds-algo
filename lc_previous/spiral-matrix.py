class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        direction = 0
        top  = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        res = []
        
        while top <= bottom and left <= right:
            # right
            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                
                top += 1
                direction = 1
            
            # Bottom
            elif direction == 1:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                
                right -= 1
                direction = 2
                
            # Left
            elif direction == 2:
                for i in reversed(range(left, right+1)):
                    res.append(matrix[bottom][i])
                bottom -= 1
                direction = 3
            
            # Top
            elif direction == 3:
                for i in reversed(range(top, bottom+1)):
                    res.append(matrix[i][left])
                
                left += 1
                direction = 0
        
        return res
                    
