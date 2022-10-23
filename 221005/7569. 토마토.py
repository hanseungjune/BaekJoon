import sys; sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline
from collections import deque

# 익은 토마토 주변에 안익은 토마토가 익음
# 방향은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
# 전부 다 익은게 몇일 걸리는지, 단 최소 일수를 구하라(BFS)
# 일부 칸에는 토마토가 없을수도 있다. -1
# 1: 익은 토마토, 0: 익지않은 토마토, -1: 없음

# 상자크기(M,N)(칸), 상자의 수(H)
M, N, H = map(int, input().split())
# 박스 쌓은거
boxes = []
# bfs를 돌릴겁니다... ㅠ 원래는 box였는데 헷갈려서 그냥 queue
queue = deque([])
# 몇일만에 번지는지 체크하는 거
cnt = 0

# 박스의 형태를 생각해...
for h in range(H):
    # 박스
    temp = []
    for n in range(N):
        temp.append(list(map(int, input().split())))
        for m in range(M):
            # 1이 있으면 해당 좌표 남기기: 이거는 토마토가 있는 순간부터 모든 토마토로 부터 번지기 때문문
            if temp[n][m] == 1:
                queue.append([h, n, m])
    # 박스안에 넣기
    boxes.append(temp)

# 3차원 방향 설정
# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [-1, 1, 0, 0, 0, 0]

# bfs
while queue:
    # 높이, 세로, 가로
    z, y, x = queue.popleft()
    for d in range(6):
        nx = x + dx[d]
        ny = y + dy[d]
        nz = z + dz[d]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and boxes[nz][ny][nx] == 0:
            # +1을 해주는 것은 번질때 (제일 큰 숫자의 -1)이 지나온 일수를 뜻하게 하려고
            boxes[nz][ny][nx] = boxes[z][y][x]+1
            queue.append([nz, ny, nx])

for box in boxes:
    for row in box:
        for col in row:
            if col == 0:
                # 0있으면 다 번진거 아니라서 -1
                print(-1)
                exit()
        # 한줄 씩 비교해서 최대값-1(최대일수) 구하기
        cnt = max(cnt, max(row))

#답
print(cnt-1)