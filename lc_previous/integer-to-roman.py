class Solution:
    
    def my_approach_enhanced(self, num):
        temp = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC':90, 'L': 50,\
            'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }
        res = []
        
        for key, val in temp.items():
            if num == 0: break
            
            cnt, num = divmod(num, val)
            res.append(cnt * key)
        
        return "".join(res)
            
    
    def my_approach (self, num):
        temp = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC':90, 'L': 50,\
            'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }
        
        res = ""
        
        while num != 0:
            for key, val in temp.items():
                if val > num:
                    continue
                cnt = num // val
                while cnt > 0:
                    num -= val
                    res += key
                    cnt -= 1
        
        return res       
    
    # my approach
    def intToRoman(self, num: int) -> str:
        return self.my_approach_enhanced(num)
