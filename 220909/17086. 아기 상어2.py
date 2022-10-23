import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
aquarium = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
distance = 0

# 상하좌우, 상좌하좌하우상우
dr = [-1,1,0,0,-1,1,1,-1]
dc = [0,0,-1,1,-1,-1,1,1]
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if aquarium[i][j] == 1:
            queue.append([i, j, distance])
            visited[i][j] = True

while queue:
    r, c, distance = queue.popleft()
    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
            queue.append([nr, nc, distance+1])
            aquarium[nr][nc] = distance+1
            visited[nr][nc] = True

print(distance)
