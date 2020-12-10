class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_map = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }
    
        
        result_map = {}
        
        for word in words:
            morse_word = ""
            for element in word:
                morse_word += (morse_map[element])  
            
            mr_c = result_map.get(morse_word)
            if not mr_c:
                result_map[morse_word] = 1
            else:
                result_map[morse_word] += 1
        # print(result_map)
        return len(list(result_map))
