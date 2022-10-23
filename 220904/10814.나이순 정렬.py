import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(str, input().split())) for _ in range(N)]
for i in range(N):
    lst[i][0] = int(lst[i][0])
for idx in range(1, N+1):
    lst[idx-1].append(idx)
    lst[idx-1][1], lst[idx-1][2] = lst[idx-1][2], lst[idx-1][1]

lst_sorted = sorted(lst)
for ls in lst_sorted:
    print(f'{int(ls[0])} {ls[2]}')
