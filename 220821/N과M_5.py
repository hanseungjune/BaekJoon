n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
answer = []

def dfs(idx, answer):
    if idx == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(n):
        if lst[i] not in answer:
            answer.append(lst[i])
            dfs(idx+1, answer)
            answer.pop()

dfs(0, answer)