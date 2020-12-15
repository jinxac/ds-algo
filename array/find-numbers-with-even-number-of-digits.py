class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for element in nums:
            if len(str(element)) % 2 == 0:
                count += 1
        
        return count 
