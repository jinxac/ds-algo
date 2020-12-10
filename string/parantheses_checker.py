def ispar(s):
    # code here
    temp = []
    for element in s:
        if element == '{' or element == '[' or element == '(':
            temp.append(element)

        elif element == '}':
            if temp and temp[-1] == '{':
                temp.pop()
            else:
                temp.append(element)

        elif element == ']':
            if temp and temp[-1] == '[':
                temp.pop()
            else:
                temp.append(element)

        elif element == ')':
            if temp and temp[-1] == '(':
                temp.pop()
            else:
                temp.append(element)


    return len(temp) == 0
