import sys; sys.stdin = open('input.txt', 'r')
import heapq

def prim(start):
    global graph
    visited[start] = 1
    heap = graph[start]
    heapq.heapify(heap)
    mst = []
    total = 0

    while heap:
        weight, u, v = heapq.heappop(heap)

        if visited[v] == 0:
            visited[v] = 1
            mst.append((u,v))
            total += weight

            for edge in graph[v]:
                if not visited[edge[2]]:
                    heapq.heappush(heap,edge)
    return total

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [0]*(V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, u, v])
    graph[v].append([w, v, u])

ans = prim(1)
print(ans)