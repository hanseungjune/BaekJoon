T = int(input())

for tc in range(1, T+1):
    N = int(input())
    sequence = list(map(int, input()))
    sum, ans = 0, 0
    for i in range(N):
        if sequence[i] == 0:
            sum = 0
            continue
        elif sequence[i] == 1:
            sum += 1
            if ans <= sum:
                ans = sum
    print(f'#{tc} {ans}')