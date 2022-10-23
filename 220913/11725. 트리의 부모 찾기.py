import sys
sys.stdin = open('input.txt', 'r')

V = int(input())
E = V - 1
tree = [[] for _ in range(V+1)]
visited = [0]*(V+1)
# 해당 번째의 노드의 부모노드를 보여줌
parents = [0]*(V+1)
stack = []

for i in range(E):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# print(tree)
def dfs(root, tree, parents):
    visited[root] = 1
    stack.append(root)
    while stack:
        x = stack.pop()
        for i in tree[x]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
                parents[i] = x

dfs(1, tree, parents)
for ans in range(2, len(parents)):
    print(parents[ans])