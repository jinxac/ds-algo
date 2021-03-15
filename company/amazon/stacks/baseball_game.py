class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for element in ops:
            if element == 'C':
                stack.pop()
                pass
            elif element == 'D':
                stack.append(stack[-1] * 2)
            elif element == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(element))
        
        return sum(stack)
