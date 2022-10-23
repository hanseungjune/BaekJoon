import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, input().split())

#각 노드의 방문 여부
visited = [0]*(N+1)

#각 노드의 인접 경로 그래프
graph = [[] for _ in range(N+1)]

cnt = 1
def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)
            
# 각 노드에 따른 인접 노드를 각 인접 노드 인덱스에 넣어주기            
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정렬해주기
for i in range(N+1):
    graph[i].sort()

dfs(graph, R, visited)

for i in range(N+1):
    if i != 0:
        print(visited[i])
