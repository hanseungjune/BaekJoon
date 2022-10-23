import heapq
# import sys; sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

st, ed = map(int, input().split())

distance = [INF]*(n+1)
def dijkstra(st):
    global distance
    distance[st] = 0
    q = [(0, st)]

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: #이미 처리되었다면 무시
            continue

        for n, d in graph[now]:
            cost = distance[now] + d
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q, (cost, n))

dijkstra(st)
print(distance[ed])