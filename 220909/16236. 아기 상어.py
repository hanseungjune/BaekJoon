import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')

N = int(input())
shark_r, shark_c = -1, -1
size, eat = 2, 0
aquarium = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]


for i in range(N):
    for j in range(N):
        if aquarium[i][j] == 9:
            shark_r, shark_c = i, j
            break
    if shark_r >= 0 and shark_c >= 0:
        break

aquarium[shark_r][shark_c] = 0

def bfs(shark_r, shark_c, size):
    visited = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append((shark_r, shark_c, 0))
    visited[shark_r][shark_c] = 1
    fish = []
    while queue:
        r, c, distance = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                visited[nr][nc] = 1
                # 먹을수 있는 조건
                if aquarium[nr][nc] != 0 and aquarium[nr][nc] < size:
                    fish.append((distance+1, nr, nc))
                    queue.append((nr, nc, distance+1))
                    visited[nr][nc] = 1
                # 방문 가능 조건
                elif aquarium[nr][nc] == 0 or aquarium[nr][nc] == size:
                    queue.append((nr, nc, distance+1))
                    visited[nr][nc] = 1

    fish.sort()
    if fish:
        return (fish[0][1], fish[0][2], fish[0][0])
    else:
        return []

total_move = 0

while True:
    fish_hunt = bfs(shark_r, shark_c, size)
    if fish_hunt:
        # 물고기 잡아 먹힌 위치랑 이동거리 반환
        x, y, move, = fish_hunt
        aquarium[x][y] = 0
        eat += 1
        # 총 이동거리 계속 더하기
        total_move += move
        if eat == size:
            size += 1
            eat = 0
        # 물고기 잡아먹은 위치에서 다시 bfs 시작
        shark_r, shark_c = x, y
    else:
        # 엄마 등장
        break

print(total_move)