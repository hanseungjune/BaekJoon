import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
time, height = 257*500*500, 0

for h in range(257):
    stock = 0
    lack = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] < h:
                lack += h-arr[i][j]
            else:
                stock += arr[i][j]-h
    if lack > stock+B:
        continue
    t = lack + stock*2
    if t <= time:
        time=t
        height=h
    if stock == 0:
        break
print(time, height)




