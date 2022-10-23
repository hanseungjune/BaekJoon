import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(node):
    # 일단 트리라고 가정
    flag = True
    queue = deque([node])
    while queue:
        x = queue.popleft()
        if visited[x] == 1:
            # 트리가 아니면
            flag = False
        visited[x] = 1
        for j in tree[x]:
            if not visited[j]:
                queue.append(j)
    return flag

tc = 0
while True:
    tc += 1
    # 노드 갯수, 간선 갯수
    V, E = map(int, input().split())
    if (V, E) == (0, 0):
        break
    # 노드 갯수만큼 자리 비워두기
    tree = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    # print(tree)

    visited = [0] * (V+1)
    cnt = 0 # 트리 갯수
    for i in range(1, V+1):
        if visited[i] == 1:
            continue
        if bfs(i) == True:
            cnt += 1

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    elif cnt >= 1:
        print(f'Case {tc}: A forest of {cnt} trees.')
