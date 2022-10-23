cal_string = input().split()
stack = []
# print(cal_string)
# print(dict)

for char in cal_string:
    if char in '(*/+-':
        if char == '(':
            stack.append(char)
        else:
            if char == '*' or char == '/':
                stack.append(char)
            else:
                if stack:
                    while True:
                        if stack[-1] == '*' or stack[-1] == '/':
                            a = stack.pop()
                            print(a, end='')
                        else:
                            stack.append(char)
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
    else:
        print(char, end='')

for remain in stack[::-1]:
    print(remain, end='')
