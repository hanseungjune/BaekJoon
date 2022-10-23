import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, input().split())

#각 노드의 방문 여부
visited = [0]*(N+1)

#각 노드의 인접 경로 그래프
graph = [[] for _ in range(N+1)]
            
# 각 노드에 따른 인접 노드를 각 인접 노드 인덱스에 넣어주기            
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정렬해주기
for i in range(N+1):
    graph[i].sort()

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = 1
    cnt = 2

    while queue:
        v=queue.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = cnt
                cnt += 1

bfs(graph, R, visited)

for i in range(N+1):
    if i != 0:
        print(visited[i])
