class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        res = []
            
        code_map = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        
        def helper(combination, pos):
            if len(combination) == len(A):
                res.append(combination)
            
            if pos >= len(A):
                return
            
            
            for element in code_map[A[pos]]:
                helper(combination + element, pos + 1)

        if not A:
            return res
            
        helper('', 0)
        
        return res

