import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

for i in lst:
    rank = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')


