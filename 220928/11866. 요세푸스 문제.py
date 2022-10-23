N, K = map(int, input().split())

lst = list(range(1, N+1))
ans = []
res = 0
k = 0
top = 0
while len(lst) != 0:
    if k == K-1:
        k = 0
        res = lst.pop(top)
        ans.append(res)
        if len(lst) == 1:
            res = lst.pop(0)
            ans.append(res)
            break
        # top -= 1
        continue

    if top == len(lst):
        if len(lst) <= 2:
            top = -2
        else:
            top = 0
    else:
        top += 1
        k += 1

answer = ', '.join(map(str, ans))
print('<', end='')
print(answer, end='')
print('>', end='')

import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
circle = deque([x for x in range(1,n+1)])
removed = []
while circle:
    circle.rotate(-(k-1))
    removed.append(circle.popleft())
print(f'<{", ".join(map(str,removed))}>')