class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        temp = keyboard.find(word[0]) # 2
        count = temp #2
        
        for i in range(1, len(word)):
            count += abs(temp - keyboard.find(word[i]))
            temp = keyboard.find(word[i]) 
        
        return count
