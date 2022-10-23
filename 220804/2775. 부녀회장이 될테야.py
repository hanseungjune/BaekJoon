import sys
import copy
input = sys.stdin.readline

answer = []

T = int(input())

for _ in range(T):
    # k층, n호
    k = int(input())
    n = int(input())

    cnt = [ i for i in range(1, n+1) ]

    if 1 <= int(k) <= 14 and 1 <= int(n) <= 14:
    # 0층
        for idx in range(1, k+1):
            next = []
            for room in range(1, n+1):
                next.append(sum(cnt[:room]))
            cnt = copy.deepcopy(next)
        answer.append(cnt[-1])

for unit in range(len(answer)):
    print(answer[unit])