class Solution:
    def anagramElegant(self,A, B):
        '''
            Learnings
            1. Short hand for creating hash table from list with index, value
            2. Short hand to check in a hash table
        '''
        temp = {x:i for i,x in enumerate(B)}
        return [temp[x] for x in A]
    
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
#         temp_map = {}
#         res = []
#         for i in range(len(B)):
#             temp_map[B[i]] = i
        
#         for element in A:
#             if element in temp_map:
#                 res.append(temp_map[element])
        
#         return res
        return self.anagramElegant(A,B)
