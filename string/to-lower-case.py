class Solution:
    def toLowerCase(self, str: str) -> str:
#         result = ""
#         for index, element in enumerate(str):
#             if 65 <= ord(element) <= 90:
#                 result += chr(ord(element) + 32)
#             else:
#                 result += element
#         return result
    
    
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        
        h = dict(zip(upper, lower))
        return ''.join([h[x] if x in h else x for x in S])
