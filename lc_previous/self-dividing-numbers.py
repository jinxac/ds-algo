class Solution:
    
    def is_number_self_divider(self, number):
        temp = number
        is_self_divider = True
        while temp > 0:
            digit = temp % 10
            if digit == 0:
                is_self_divider = False
                break
            if number % digit != 0:
                is_self_divider = False
                break
            temp = temp // 10
        
        return is_self_divider
            
    
        
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for element in range(left, right + 1):
            is_self_dividing = self.is_number_self_divider(element)
            if is_self_dividing:
                result.append(element)
        
        return result
            
