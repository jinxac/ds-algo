class Solution:
    def sliding_way(self, s):
        start = 0
        end = 0
        res = 0
        temp = {}

        while end < len(s):
            if s[end] in temp:
                res = max(res, end - start)
                while s[end] in temp:
                    del temp[s[start]]
                    start += 1
            temp[s[end]] = 1
            end += 1

        res = max(res, end - start)
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.sliding_way(s)