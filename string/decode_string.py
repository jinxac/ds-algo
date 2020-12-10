"""
https://leetcode.com/problems/decode-string/
"""

class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, element):
        self.arr.append(element)
        self.top += 1

    def pop(self):
        element = self.arr.pop()
        self.top -= 1
        return element

    def isFull(self):
        return self.top >= len(self.arr) - 1

    def isEmpty(self):
        return self.top == -1

    def IsStartBracket(self):
        return self.arr[self.top] == '['

    def isDigit(self):
        return self.arr[self.top].isdigit()


class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        # stack = []
        i = 0
        stack = Stack()

        while i < len(s):
            if s[i] == ']':
                temp = ""
                while not stack.isEmpty() and not stack.IsStartBracket():
                    temp =  stack.pop() + temp

                stack.pop() #removing opening bracket
                count = ""
                while not stack.isEmpty() and stack.isDigit():
                    count = stack.pop() + count

                temp = temp * int(count)

                if not stack.isEmpty():
                    pos = 0
                    while pos < len(temp):
                        stack.push(temp[pos])
                        pos += 1
                else:
                    res += temp
            else:
                stack.push(s[i])

            i += 1

        temp = ""
        while not stack.isEmpty():
            temp = stack.pop() + temp

        res += temp

        return res