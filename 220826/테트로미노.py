import sys
sys.stdin = open('input.txt','r')

def fucku(r, c):
    fuck_lst = []
    global N, M, answer
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            fuck_lst.append(arr[nr][nc])

    if len(fuck_lst) >= 3:
        sumV = arr[r][c] + sum(sorted(fuck_lst, reverse=True)[:3])
        answer = max(sumV, answer)

def dfs(r, c, step, total):
    global N, M, answer
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    if step == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc, step+1, total+arr[nr][nc])
                visited[nr][nc] = 0

######################################################################

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0
        fucku(i, j)

print(answer)