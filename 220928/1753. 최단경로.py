import sys; sys.stdin=open('input.txt','r')
#
# def dijkstra(S, V):
#     visited[S] = 1
#     distance[S] = 0
#     for v, w in adjL[S]:
#         distance[v] = w
#
#     for _ in range(V):
#         minV = INF
#         t = 0
#         for i in range(V+1):
#             if visited[i] == 0 and minV > distance[i]:
#                 minV = distance[i]
#                 t = i
#         visited[t] = 1
#         for v, w in adjL[t]:
#             distance[v] = min(distance[v], distance[t]+w)
#
# # 초반세팅
# V, E = map(int, input().split())
# S = int(input())
# adjL = [[] for _ in range(V+1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjL[u].append([v, w])
#
# INF = 1e9
# # 시작점과의 거리
# distance = [INF]*(V+1)
# # 해당 정점에서 방문했는지 확인(똑같은 곳 굳이 할필요 없다는 생각)
# visited = [0]*(V+1)
# ######
# dijkstra(S, V)
# for d in range(1, len(distance)):
#     if distance[d] == 1e9:
#         print('INF')
#     else:
#         print(distance[d])

# 초반 세팅
import sys
input = sys.stdin.readline
import heapq
INF = 1e9
V, E = map(int, input().split())
S = int(input())
distance = [INF]*(V+1)
adjL = [[] for _ in range(V+1)]
# 연결리스트에 인접노드 설정하기
for _ in range(E):
    u, v, w = map(int, input().split())
    adjL[u].append((w, v))

# 다익스트라 힙으로 하였음(힙을 쓰면 앞에있는 요소(가중치)에 따라서 작은걸 먼저 돌려볼수 있기에 가지치기하는데 적함
def dijkstra(s):
    heap = []
    # 지가 지한테는 0이지
    distance[s] = 0
    # 시작!
    heapq.heappush(heap, (0, s))
    while heap:
        dist, node = heapq.heappop(heap)
        # 이거 없어서 시간초과 많이남(가지치기)
        # 계속 이어지다가 시작점에서 해당노드까지 이미 dist보다 더 작은애 있을수 있으니 더이상 진행은 의미 없음
        if distance[node] < dist:
            continue
        # 인접리스트에 해당 노드 연결되어있는지 확인
        for w, v in adjL[node]:
            # 돌아가능 경우 거리 합
            cost = dist + w
            # distance[v]는 다이렉트 거리
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(heap, (distance[v], v))

dijkstra(S)
# 출력 방식
# print(distance)
for d in range(1, len(distance)):
    if distance[d] == 1e9:
        print('INF')
    else:
        print(distance[d])