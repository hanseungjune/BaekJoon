import sys
sys.stdin = open('input.txt', 'r')

# 재귀로 리프노드까지 모두 -100처리
def dfs(x):
    global V
    parents[x] = -100
    for i in range(V):
        if x == parents[i]:
            dfs(i)

# 노드의 갯수
V = int(input())
# 노드마다 1씩 더해준 것
parents = list(map(int, input().split()))
# print(parents)
# 지울 노드
x = int(input())
cnt = 0
dfs(x)
# print(parents)
# 1) -100처리 된거 제외, 2)부모노드로서 역할하는 애들 제외 카운팅
for i in range(V):
    if parents[i] != -100 and i not in parents:
        cnt += 1
print(cnt)