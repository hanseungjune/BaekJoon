import sys; sys.stdin=open('input.txt','r')
from collections import deque
# 걸으면 X+1 or X-1
# 순간이동 2*X

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            break

        for j in (x-1, x+1, x*2):
            if 0 <= j <= max_len and not visited[j]:
                visited[j] = visited[x] + 1
                queue.append(j)

# 수빈이 위치, 동생 위치
max_len = 100000
N, K = map(int, input().split())
visited = [0] * (max_len+1)

bfs()