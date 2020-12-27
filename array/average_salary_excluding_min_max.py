"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""

class Solution:
    def average(self, salary: List[int]) -> float:
        min_val = min(salary)
        max_val = max(salary)

        val = sum(salary) - min_val - max_val

        return val / (len(salary) - 2)