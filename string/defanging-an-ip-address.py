import re

class Solution:
    '''
        Solution:
            1. Use regex to substitute
            2. Use string to replace
            3. Split on . and join using [.]
        Learnings:
            1. Python regex
    '''
    def defangIPaddr(self, address: str) -> str:
        return re.sub("\.", "[.]", address)
        
