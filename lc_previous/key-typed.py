class Solution:
    '''
    Observations:
        1. Was able to figure out that we can use hashmaps for this
        2. Solution works for 65/72 cases
        3. Missed few cases where same character is repeated again after few other characters
            "abca"
            "aabbcc"
            
    Learnings:
        1. Learnt about group by, itertools
        2. group by function of python
        3. Two pointer approach
        
    Edge cases:-
    
        1. If length of first string is less than second string and last character is not                  repeated
        2. If length of first string is less than second string and last character is repeated            but the typed string has few more characters in the end which first string does not            have.
        
    2 pointer algorithm:-
    
        1. Check if both element at index i of name and index j of typed is equal.
        2. If it is equal increment i and j
        3. If not, compare with previous element. If equal increment j, else return False
        4. Check for corner cases, string beginning, string end.
        
        
    '''
    def groupName(self, name, typed):
        g1 = []
        g2 = []
        
        for k,g in itertools.groupby(name):
            g1.append((k,len(list(g))))
        
        for k, g in itertools.groupby(typed):
            g2.append((k, len(list(g))))

        
        if len(g1) != len(g2):
            return False
        
        for i in range(len(g1)):
            if g1[i] > g2[i]:
                return False
        
        return True
        
    
    
    def twoPointerName(self, name, typed):
        i = 0
        j = 0
        
        if name[i] != typed[j]:
            return False
        
        
        if name == typed:
            return True
        
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif typed[j] == name[i-1]:
                j += 1
            else:
                return False
        
        if i < len(name):
            return False
        
        while j < len(typed):
            if typed[j] != name[i-1]:
                return False
            j += 1
        
        return True
    
    
    def twoPointerSmartName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)
    
    def isLongPressedName(self, name: str, typed: str) -> bool:
        return self.twoPointerSmartName(name, typed)
