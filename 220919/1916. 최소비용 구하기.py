import sys
sys.stdin = open('input.txt', 'r')

# 도시의 개수
city = int(input())
# 버스의 개수
bus = int(input())
# 노드(도시)간의 연결 리스트
graph = [[] for _ in range(city+1)]
visited = [0]*(city+1)
distance = [1e9]*(city+1)

for _ in range(bus):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 출발, 도착
start, end = map(int, input().split())

# 거리가 가장 짧은 노드 구하기
def smallest_distance(city):
    mn = 1e9
    index = 0
    for stop in range(1, city+1):
        if not visited[stop] and distance[stop] < mn:
            mn = distance[stop]
            index = stop
    return index

def dijkstra(start, end):
    global city
    # 일단 방문처리랑 출발에서 출발
    distance[start] = 0
    visited[start] = 1
    for i in graph[start]:
        # 거리 업데이트 해버리기~~~
        if distance[i[0]] > i[1]:
            distance[i[0]] = i[1]

    # 이제 반복 돌릴건데 출발은 제외해버리기
    for _ in range(city-1):
        # 지금 제일 거리 가까운 노드 뭥미?
        now = smallest_distance(city)
        visited[now] = 1
        if now == end:
            break
        for next in graph[now]:
            dist = distance[now] + next[1]
            if dist < distance[next[0]]:
                distance[next[0]] = dist

    return distance[end]

print(dijkstra(start, end))


