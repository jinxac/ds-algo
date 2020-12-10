class Solution:
    def numberOfSteps (self, num: int) -> int:
        '''
            Learnings: Time complexity
            
            At each step, what we did depended on whether the remaining numnum was odd or even. If numnum was even, we halved what was left. If it was odd, we only subtracted 1. However, by subtracting 1, we were making it even, and so on the next step we were guaranteed to halve it.
        '''
        cnt = 0 
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            
            cnt += 1
        
        return cnt
                
