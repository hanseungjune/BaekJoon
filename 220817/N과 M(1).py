n, m = map(int, input().split())
answer = []

def dfs(idx):
    if idx == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            dfs(idx+1)
            answer.pop()

dfs(0)