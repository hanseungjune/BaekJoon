N, M = map(int, input().split())
answer = []

def dfs(start):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, N+1):
        if i not in answer:
            answer.append(i)
            # start 말고 i를 넣어야 i 다음으로 나오는 숫자를 채택할 수 있음
            dfs(i+1)
            answer.pop()

dfs(1)
