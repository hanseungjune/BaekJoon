import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('1012.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    def dfs(m, n):
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]

        for i in range(4):
            ny = n + dy[i]
            nx = m + dx[i]
            if (0 <= ny <= N-1) and (0 <= nx <= M-1):
                if visited[ny][nx] == 1:
                    visited[ny][nx] = -1
                    dfs(nx, ny)

    M, N, K = map(int, input().split())
    visited = [[0]*M for _ in range(N)]

    for k in range(K):
        m, n = map(int, input().split())
        visited[n][m] = 1

    cnt = 0
    for n in range(N):
        for m in range(M):
            if visited[n][m] == 1:
                dfs(m, n)
                cnt += 1

    print(cnt)