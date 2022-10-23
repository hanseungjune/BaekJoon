import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

K, N = map(int, input().split())
LANs = [int(input()) for _ in range(K)]
start, end = 1, max(LANs)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in LANs:
        cnt += i // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)