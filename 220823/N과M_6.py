import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
result = list(map(int, input().split()))
result.sort()
stack = []

def dfs(idx, start):
    global N, M, stack
    if idx == M:
        print(*stack)
        return

    for i in range(start, N):
        if result[i] not in stack:
            stack.append(result[i])
            dfs(idx+1, i+1)
            stack.pop()

dfs(0, 0)