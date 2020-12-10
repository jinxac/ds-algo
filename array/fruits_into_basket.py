"""
https://leetcode.com/problems/fruit-into-baskets/
"""


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        start = 0
        end = 0
        temp = {}
        res = 0

        while end < len(tree):
            if not tree[end] in temp:
                temp[tree[end]] = 0

            temp[tree[end]] += 1

            while len(temp) > 2:
                res = max(res, end - start)
                temp[tree[start]] -= 1
                if temp[tree[start]] == 0:
                    del temp[tree[start]]

                start += 1

            end += 1

        res = max(res, end - start)
        return res