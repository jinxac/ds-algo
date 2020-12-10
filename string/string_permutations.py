class Solution:
    def solve(self, s):
        self.res = ""
        list_s = []
        list_s[:0] = s
        def traverse(start):
          if start == len(list_s) - 1:
            self.res += ''.join(list_s) + " "
            # self.res.append(''.join(list_s))
            return

          for i in range(start, len(list_s)):
            list_s[i], list_s[start] = list_s[start], list_s[i]
            traverse(start + 1)
            list_s[i], list_s[start] = list_s[start], list_s[i]

        traverse(0)
        return self.res.strip()



if __name__ == "__main__":
    t = int(input())

    while t > 0:
        string = input()
        s = Solution()
        print(s.solve(string))
        t -= 1