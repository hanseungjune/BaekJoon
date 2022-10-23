import sys
sys.stdin = open('고대유적.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))[:M] for _ in range(N)]

    ans = 0
    for i in range(N):
        Mx_row = 0
        for j in range(M):
            if arr[i][j] == 1:
                Mx_row += 1
                if ans < Mx_row:
                    ans = Mx_row
            elif arr[i][j] == 0:
                Mx_row = 0

    res = 0
    for j in range(M):
        Mx_col = 0
        for i in range(N):
            if arr[i][j] == 1:
                Mx_col += 1
                if res < Mx_col:
                    res = Mx_col
            elif arr[i][j] == 0:
                Mx_col = 0

    if ans > res:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {res}')

