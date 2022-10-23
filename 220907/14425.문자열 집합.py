import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
set_s = set(input() for _ in range(N))

cnt = 0
for _ in range(M):
    j = input()
    if j in set_s:
        cnt += 1
print(cnt)