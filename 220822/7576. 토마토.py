import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs():
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<M and 0<=nc<N and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c]+1
                queue.append([nr, nc])

N, M = map(int, input().split())
#N은 가로, M은 세로
arr = [list(map(int, input().split())) for _ in range(M)]
queue = deque([])

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            queue.append([i, j])

bfs()
result = 0
for row in arr:
    for col in row:
        if col == 0:
            print(-1)
            exit(0)
    result = max(result, max(row))
print(result-1)



