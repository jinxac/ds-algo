"""
https://leetcode.com/problems/xor-operation-in-an-array/
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for i in range(n):
            arr.append(start + 2*i)


        res = arr[0]
        for i in range(1, len(arr)):
            res ^= arr[i]

        return res