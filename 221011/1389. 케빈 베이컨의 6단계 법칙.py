import sys; sys.stdin=open('input.txt','r')

def dfs(st, en, length):
    global graph, visited, score
    if st == en:
        score = length
        return

    visited[st] = 1
    for ele in graph[st]:
        if not visited[ele]:
            dfs(ele, en, length+1)

# 유저의 수, 친구 관계의 수
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for e in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# for row in graph:
#     print(row)

# 케빈 베이컨의 수 넣는 배열
res = []
for i in range(1, N+1):
    score = 0
    sm = 0
    for j in range(1, N+1):
        visited = [0] * (N + 1)
        if i == j:
            continue
        else:
            dfs(i, j, 0)
            sm += score
            score = 0
    else:
        res.append(sm)

# print(res)

result = 0
ans = min(res)
for i in res:
    if ans == i:
        result += res.index(i)
        break

print(result+1)