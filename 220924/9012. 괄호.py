import sys; sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    stack = []
    bracket = list(input())
    flag = False

    for b in bracket:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if '(' in stack:
                stack.pop()
            elif '(' not in stack:
                flag = True

    if len(stack)>=1 or flag:
        print('NO')
    else:
        print('YES')
