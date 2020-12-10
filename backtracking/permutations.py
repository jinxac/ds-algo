class Solution:
    def solve(self, s):
        arr_s = [x for x in s]
        self.res = ""

        def traverse(start):
            if start == len(arr_s) - 1:
                self.res = self.res + ''.join(arr_s) + " "
                return

            for i in range(start, len(arr_s)):
                arr_s[i], arr_s[start] = arr_s[start], arr_s[i]
                traverse(start + 1)
                arr_s[i], arr_s[start] = arr_s[start], arr_s[i]

        traverse(0)
        print(self.res.strip())


if __name__ == "__main__":
    t = int(input())

    while t > 0:
        string = input()
        s = Solution()
        s.solve(string)
        t -= 1