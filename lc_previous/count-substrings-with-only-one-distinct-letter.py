from itertools import groupby

class Solution:
    def spaceEfficientSolution(self, S):
        count=0
        total=0
        pre=0
        for i in range(len(S)):
            if S[i]==S[pre]:
                count+=1
            else:
                count=1
            pre = i
            total+=count
        return total
    
    
    def groupBySolution (self, S):
        arr = [element for element in S]
        temp = []
        res = 0
        for key, group in groupby(arr):
            temp.append(list(group))
        
        for row in temp:
            len_row = len(row)
            res += (len_row * (len_row + 1)) // 2
        
        return res  
    
    def countLetters(self, S: str) -> int:
        return self.groupBySolution(S)
