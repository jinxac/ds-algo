class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:        
        hc.sort()
        vc.sort()
        
        height = max(hc[0], h - hc[-1])
        width = max(vc[0], w - vc[-1])
        
        
        
        for i in range(len(hc) - 1):
            diff = hc[i+1] - hc[i]
            height = max(height, diff)
            
        for i in range(len(vc) - 1):
            diff = vc[i+1] - vc[i]
            width = max(width, diff)
            
    
        
        return (width * height) % 1000000007
