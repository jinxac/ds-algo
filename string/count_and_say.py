class Solution:
    def convert_string(self, string):
        i = 0
        temp = ""
        while i < len(string):
            j = i + 1
            while j < len(string) and string[i] == string[j]:
                j += 1
            temp += str(j-i) + string[i]
            i = j

        return temp

    def bottom_up_approach(self, n):
        res = "1"

        while n > 1:
            res = self.convert_string(res)
            n -= 1

        return res



    def countAndSay(self, n: int) -> str:
        return self.bottom_up_approach(n)

        if n == 1:
            return "1"
        else:
            t = self.countAndSay(n-1)
            return self.convert_string(t)
