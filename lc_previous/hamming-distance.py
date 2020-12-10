class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x > 0 or y > 0:
            x_bit = x & 1 
            y_bit = y & 1
            if x_bit != y_bit:
                count += 1
            x = x >> 1
            y = y >> 1
        
        return count
        
