from collections import deque
import sys
sys.stdin = open('24444.txt', 'r')

n, m, r = map(int, sys.stdin.readline().split()) # n: 정점/ m: 간선/ r: 시작 정점
# graph 만들기
graph = [[]]
for i in range(1, n+1):
    graph.append([])
# 입력받은 값 넣어주기
for j in range(n):
    a, b = map(int,  sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for idx in range(n+1):
    graph[idx].sort()

# 방문기록
visited = [False]*(n+1)
# 몇번째 방문인지 기록
turn = deque([0]*(n+1))
# 탐색 시작
node = r
queue = deque([node])
visited[node] = True
cnt = 1
turn[node] = cnt           # 각 노드의 나간 순서

while queue:
    v = queue.popleft()
    for k in graph[v]:
        if not (visited[k]):
            queue.append(k)
            visited[k] = True
            cnt += 1
            turn[k] = cnt

for num in range(n+1):
    if num != 0:
        print(turn[num])