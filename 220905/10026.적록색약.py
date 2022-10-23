import sys
from collections import deque
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

def bfs():
    global i, j, visited, cnt, medicine
    nr, nc = i, j
    queue = deque([[nr, nc]])

    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] == medicine and visited[nr][nc] == 0:
                queue.append([nr, nc])
                visited[nr][nc] = cnt

# 줄의 수
N = int(input())
# 검토해야할 배열
arr = [list(map(str, input())) for _ in range(N)]
# 방문처리용 구역 나누기용
cnt = 1
# 방문처리요~~
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and (arr[i][j] == 'R' or arr[i][j] == 'G' or arr[i][j] == 'B'):
            medicine = arr[i][j]
            bfs()
            cnt += 1
first = cnt-1
# 이제 색약애들
cnt = 1
# G를 전부 R로 바꾸기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

# 이제 색약 방문처리
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and (arr[i][j] == 'R' or arr[i][j] == 'B'):
            medicine = arr[i][j]
            bfs()
            cnt += 1
second = cnt-1
print(f'{first} {second}')
