import sys; sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt0 = [1, 0]
    cnt1 = [0, 1]
    if n > 1:
        for i in range(n-1):
            cnt0.append(cnt1[-1])
            cnt1.append(cnt0[-2]+cnt1[-1])

    print(f'{cnt0[n]} {cnt1[n]}')