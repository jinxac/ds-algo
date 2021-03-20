class Solution:
    
    def base_map(self, num):
        switcher = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        
        return switcher.get(num)
    
    def ten_map(self, num):
        switcher = {
            1: 'Ten',
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety',
            0: 'Hundred'
        }
        
        return switcher.get(num)
    
    def two(self, num):
        if num < 20:
            return self.base_map(num)
        
        
        div, mod = divmod(num , 10)
        if div and mod:
            return self.ten_map(div) + ' ' + self.base_map(mod)
        
        if div and not mod:
            return self.ten_map(div)
            
        
    
    def three(self, num):
        div, mod = divmod(num, 100)
        
        if div and mod:
            return self.two(div) + ' Hundred ' + self.two(mod)
        if not div and mod:
            return self.two(mod)
        
        return self.two(div) + ' Hundred'
        
    def numberToWords(self, num: int) -> str:
        result = ''
        
        if not num:
            return "Zero"
        
            
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = (num - billion * 1000000000 - million * 1000000 - thousand * 1000)
        
        
        if billion:
            result += self.three(billion) + ' ' + 'Billion'
            
        if million:
            if result: result += ' '
            result += self.three(million) + ' ' + 'Million'
        
        if thousand:
            if result: result += ' '
            result += self.three(thousand) + ' ' + 'Thousand'
            
        if rest:
            if result: result += ' '
            result += self.three(rest)
        
        return result
