import sys; sys.stdin = open('input.txt', 'r')

T = int(input())
stack = []
for b in range(T):
    number = input()
    if stack and number == '0':
        stack.pop()
    elif not stack and number == '0':
        continue
    else:
        stack.append(number)

ans = 0
for s in stack:
    ans += int(s)

print(ans)
