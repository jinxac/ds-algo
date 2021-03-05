class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        temp = {}
        res = []
        
        for index, element in enumerate(A):
            diff = B - element
            if diff in temp and temp[diff] != index + 1:
                res.append([temp[diff], index + 1])
                # return [temp[diff], index + 1]
            
            temp[element] = index + 1
        
        print("here", res)
        return []
