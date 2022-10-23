import sys
sys.stdin = open('input.txt','r')

n = int(input())
lst = [int(input()) for x in range(n)]
stack = []
ans = []
res = []
i = 1
for num in lst:
    while i < n+1:
        if stack and stack[-1] == num:
            rem = stack.pop()
            res.append(rem)
            ans.append('-')
            break
        elif i not in stack:
            stack.append(i)
            ans.append('+')
            i += 1
for i in range(len(stack)):
    res.append(stack.pop())
    ans.append('-')

if res == lst:
    for p in ans:
        print(p)
else:
    print('NO')


