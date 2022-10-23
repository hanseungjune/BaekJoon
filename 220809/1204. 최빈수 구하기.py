import sys
sys.stdin = open('input(1).txt', 'r')

T = int(input())


for tc in range(1, T+1):
    tc = int(input())

    score = [0] * 101
    lst = list(map(int, input().split()))

    for i in lst:
        score[i] += 1

    mx = score[0]
    idx = 0
    for i in range(1, 101):
        if mx < score[i]:
            mx = score[i]
            idx = i

    print(f'#{tc} {i}')