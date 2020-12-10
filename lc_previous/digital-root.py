class Solution:
    

    # Recursion solution
#     def add(num):
#         if num <= 9:
#             return num
#         s = 0
#         while num > 0:
#             s += num % 10
#             num = num // 10

#         return add(s)

#     return add(num)

    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num % 9 == 0:
            return 9
        
        return num % 9

    
        
