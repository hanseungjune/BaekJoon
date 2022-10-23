import sys
import copy
# sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs():
    global arr, queue
    test_arr = copy.deepcopy(arr)
    for o in range(N):
        for p in range(M):
            if arr[o][p] == 2:
                queue.append((o, p))
    cnt = 0
    # 상우하좌
    delta = [(-1,0), (0,1), (1,0), (0,-1)]

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            dy, dx = delta[d][0], delta[d][1]
            ny = y+dy
            nx = x+dx
            if (ny >= 0 and ny < N and nx >= 0 and nx < M) and test_arr[ny][nx] == 0:
                test_arr[ny][nx] = 2
                queue.append((ny, nx))
    global result
    for row in range(N):
        for col in range(M):
            if test_arr[row][col] == 0:
                cnt += 1
    result = max(result, cnt)

def make_wall(count):
    global queue, N, M
    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                make_wall(count+1)
                arr[i][j] = 0
# N은 세로, M은 가로
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
queue = deque()

make_wall(0)
print(result)