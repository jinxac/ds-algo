class Solution:
    def trap(self, height):
        res = 0
        
        if not height:
            return res
        
        max_left = [float('-inf')] * len(height)
        max_right = [float('-inf')] * len(height)
        
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i-1])
            
            
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])
            
        
        for i in range(0, len(height)):
            diff = min(max_left[i], max_right[i])
            res += diff - height[i]
                
        
        return res
