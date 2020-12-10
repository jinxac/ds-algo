"""
https://leetcode.com/problems/partition-labels/
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_count = [0] * 26
        res = []

        for i in range(len(S)):
            last_count[ord(S[i]) - 97] = i


        start = 0
        partition_count = 0
        anchor = 0

        while start < len(S):
            partition_count = max(last_count[ord(S[start]) - 97], partition_count)
            if start == partition_count:
                res.append(partition_count - anchor + 1)
                anchor = start + 1

            start += 1

        return res