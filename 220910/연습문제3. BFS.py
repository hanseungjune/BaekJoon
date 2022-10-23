import sys
sys.stdin = open('input.txt', 'r')

graph = [[] for _ in range(8)]
node_lst = list(map(int, input().split()))
for i in range(0, len(node_lst), 2):
    a, b = node_lst[i], node_lst[i+1]
    graph[a].append(b)
    graph[b].append(a)

v = 1
queue = []
visited = [0]*8
print(v, end=' ')
def bfs(v):
    global graph, queue, visited
    queue.append(v)
    visited[v] = 1
    while queue:
        r = queue.pop(0)
        for j in graph[r]:
            if not visited[j]:
                visited[j] = 1
                print(j, end=' ')
                queue.append(j)

bfs(v)