class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split('.')]
        
        p1 = 0
        p2 = 0
        l_p1 = len(v1)
        l_p2 = len(v2)
        
        if l_p1 < l_p2:
            v1 += [0] * (l_p2 - l_p1)
        else:
            v2 += [0] * (l_p1 - l_p2) 
                        
        while p1 < len(v1):
            diff = v1[p1] - v2[p2]
            if diff < 0:
                return -1
            
            if diff > 0:
                return 1
            
            p1 += 1
            p2 += 1
            
        return 0
