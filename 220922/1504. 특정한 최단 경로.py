import heapq
# import sys; sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())
INF = 1e9
graph = [[] for _ in range(N+1)]
visited = []
for _ in range(M):
    #a번 노드에서 b번 노드로 c비용만큼 연결
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 1번에서 N번으로
def dijkstra(st):
    global ess1, ess2
    distance = [1e9] * (N + 1)
    distance[st] = 0
    q = [(0, st)]

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for n, d in graph[now]:
            cost = distance[now] + d
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))

    return distance

# 반드시 거쳐야할 노드
ess1, ess2 = map(int, input().split())
origin_distance = dijkstra(1)
ess1_dist = dijkstra(ess1)
ess2_dist = dijkstra(ess2)
path1 = origin_distance[ess1] + ess1_dist[ess2] + ess2_dist[N]
path2 = origin_distance[ess2] + ess2_dist[ess1] + ess1_dist[N]

res = min(path1, path2)
print(res if res < INF else -1)