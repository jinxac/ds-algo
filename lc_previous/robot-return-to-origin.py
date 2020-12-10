class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x =  0 
        y =  0
        for element in moves:
            if element == "U":
                y += 1
            elif element == "D":
                y -= 1
            elif element == "L":
                x -= 1
            elif element == "R":
                x += 1
        
        return x == 0 and y == 0
                
        
