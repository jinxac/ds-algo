class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_element = -1
        res = []
        for element in candies:
            if max_element < element:
                max_element = element
        
        
        for element in candies:
            if extraCandies + element >= max_element:
                res.append(True)
            else:
                res.append(False)
        
        return res
