'''
 Things learnt:
 
   1. divmod
   2. Log 10 efficiency (N is the number because each digit represents {digit}*10^(k-th location)
''' 

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summation = 0
        product = 1
        while n:
            n, digit = divmod(n, 10)
            summation += digit
            product *= digit
        
        return product - summation
