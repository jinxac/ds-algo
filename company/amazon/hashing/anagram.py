class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        res = []
        temp = {}
        
        for index, element in enumerate(A):
            key = ''.join(sorted(list(element)))
            if not key in temp:
                temp[key] = []
            
            temp[key].append(index + 1)
        
        for value in temp.values():
            res.append(value)
            
        return res
            

