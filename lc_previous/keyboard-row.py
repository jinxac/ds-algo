class Solution:
    def my_method(self, words):
        tmp = {
            'q': 1,
            'w': 1,
            'e': 1,
            'r': 1,
            't': 1,
            'y': 1,
            'u': 1,
            'i': 1,
            'o': 1,
            'p': 1,
            'a': 2,
            's': 2,
            'd': 2,
            'f': 2,
            'g': 2,
            'h': 2,
            'j': 2,
            'k': 2,
            'l': 2,
            'z': 3,
            'x': 3,
            'c': 3,
            'v': 3,
            'b': 3,
            'n': 3,
            'm': 3
        }

        def word_check_new(string):
            l_string = len(string)
            string = string.lower()
            if not string or l_string == 1:
                return True

            actual_sum = 0
            expected_sum = tmp[string[0]] * l_string
            for element in string:
                actual_sum += tmp[element]


            return actual_sum == expected_sum


        for element in words:
            if word_check_new(element):
                res.append(element)

        return res

    def findWords(self, words: List[str]) -> List[str]:
        return self.my_method(words)
