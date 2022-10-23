import sys;sys.stdin=open('input.txt','r')
from collections import deque

def dfs(V):
    global visited, graph
    visited[V] = 1
    for i in graph[V]:
        if not visited[i]:
            print(i, end=' ')
            dfs(i)

def bfs(V):
    global visited, graph
    queue = deque([V])
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                print(i, end=' ')
    print()

#정점의 개수, 간선의 개수, 정점의 번호(출발)
N, M, V = map(int, input().split())
visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for m in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

for row in graph:
    row.sort()

# for row in graph:
#     print(row)

print(V, end=' ')
visited[V] = 1
dfs(V)
print()
visited = [0]*(N+1)
print(V, end=' ')
visited[V] = 1
bfs(V)