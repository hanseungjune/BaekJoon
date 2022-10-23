import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 단지 가로 세로, 집이있는 위치는 1, 방문여부 체크
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    visited[r][c] = 1
    global apartment #아파트의 갯수
    if graph[r][c] == 1:
        apartment += 1
    # 방향 설정하고 주변에 1있는지 확인하기
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if visited[nr][nc] == 0 and graph[nr][nc] == 1:
                dfs(nr, nc)

apartment = 0 # 해당 단지의 아파트 수
result = [] # 단지별 아파트 숫자 넣기
# 시작은 0,0
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1 and visited[r][c] == 0:
            dfs(r, c)
            result.append(apartment)
            apartment = 0

# 아파트 단지 수
print(len(result))
for i in sorted(result):
    print(i)


