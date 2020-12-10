class Solution:
    '''
        Testcases checked:-
        
        1. Single character word
        2. Single character equal words
        3. First word is substring of second word
        4. Both words are equal
        5. First character of words match and return
        6. First word partially matches second word
        
        Missed testcases:-
        
        1. single character in which first character is of higher order
    '''
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        tmp = {}
        for i in range(len(order)):
            tmp[order[i]] = i
        
        def cmp(word1, word2):                        
            i = 0
            j = 0
            
            while i < len(word1) and j < len(word2):
                if tmp[word1[i]] < tmp[word2[j]]:
                    return True
                elif tmp[word1[i]] > tmp[word2[j]]:
                    return False
                i += 1
                j += 1
            
            if i < len(word1):
                return False
            
            return True
        
        for i in range(len(words) - 1):
            if not cmp(words[i], words[i+1]):
                return False
        
        return True
            
