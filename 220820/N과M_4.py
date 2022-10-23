n, m = map(int, input().split())
answer = []

def dfs(idx, start):
    if idx == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, n+1):
        answer.append(i)
        dfs(idx+1, i)
        answer.pop()

dfs(0, 1)