import sys
from collections import deque
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
# 100~105면 도착임
game = [0] * 106
visited = [0] * 106
for _ in range(N+M):
    start, end = list(map(int, input().split()))
    game[start] = end
queue = deque()
# (주사위 던진 횟수, 출발 위치)
queue.append((0, 1))
visited[1] = 1

while queue:
    cnt, which = queue.popleft()
    if which >= 100:
        print(cnt)
        break
    cnt += 1
    for i in range(1, 7):
        which_dice = which+i
        if visited[which_dice]:
            continue
        visited[which_dice] = 1
        if game[which_dice]:
            queue.append((cnt, game[which_dice]))
        else:
            queue.append((cnt, which_dice))
