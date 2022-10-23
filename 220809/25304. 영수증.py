import sys
input = sys.stdin.readline

total = int(input())
T = int(input())

sum = 0
for _ in range(T):
    a, b = map(int, input().split())
    sum += (a*b)

if sum == total:
    print('Yes')
else:
    print('No')