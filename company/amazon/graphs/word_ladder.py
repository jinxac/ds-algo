class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dq = deque()
        temp_map = {datum: None for datum in wordList}
        level = 0
        
        if beginWord in temp_map:
            del temp_map[beginWord]
            
        dq.appendleft(beginWord)
        
        while dq:
            dq_size = len(dq)
            level += 1
            
            for _ in range(dq_size):
                element = dq.pop()
                if element == endWord:
                    return level
                combination_words = self.get_combinations(element)
                for combination in combination_words:
                    if combination in temp_map:
                        dq.appendleft(combination)
                        del temp_map[combination]
                        
        return 0
    
    def get_combinations(self, word):
        result = []
        
        for i in range(len(word)):
            for pos in range(26):
                temp = word[:i] + chr(ord('a') + pos) + word[i+1:]
                if temp != word:
                    result.append(temp)
        
        return result
