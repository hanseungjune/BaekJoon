import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

arr = sorted(lst)
for i in arr:
    print(f'{i[0]} {i[1]}')
