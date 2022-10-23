import sys
input = sys.stdin.readline
# sys.stdin = open('input1.txt', 'r')

N = int(input())
M = int(input())

visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

def dfs(graph, R, visited):
    visited[R] = 1
    for j in graph[R]:
        if visited[j] == 0:
            dfs(graph, j, visited)

dfs(graph, 1, visited)

print(sum(visited)-1)