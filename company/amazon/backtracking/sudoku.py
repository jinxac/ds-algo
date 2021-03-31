class Solution:
    def is_valid(self, board, x, y, num):
        for i in range(len(board)):
            if board[i][y] == num:
                return False
        
        for j in range(len(board[0])):
            if board[x][j] == num:
                return False
        
        sub_x = (x // 3) * 3
        sub_y = (y // 3) * 3
        
        for i in range(3):
            for j in range(3):
                if board[i+sub_x][j+sub_y] == num:
                    return False
        
        return True
            
            
            
    def helper(self, board, x, y):   
        if x == len(board):
            return True
            # print("bazinga", board)
            # return    
        
        curr_x = 0
        curr_y = 0
        
        
        if y == len(board[0]) - 1:
            curr_x = x + 1
            curr_y = 0
        else:
            curr_y = y + 1
            curr_x = x
            
        
        if board[x][y] != '.':
            return self.helper(board, curr_x, curr_y)
        else:
            for num in range(1, 10):
                val = str(num)
                if self.is_valid(board, x, y, val):
                    board[x][y] = val
                    if self.helper(board, curr_x, curr_y):
                        return True
                    board[x][y] = '.'

            return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(board, 0, 0)
        
